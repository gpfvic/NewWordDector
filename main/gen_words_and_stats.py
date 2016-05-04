# -*- coding: utf-8 -*-  
'''
Created on 2016年1月7日

@author: gaopengfei
'''
import sys, sqlite3, os, subprocess
import multiprocessing
import vtools, Stats
from Word import Word

############################
stats = Stats.Stats()
PARALLEL_NUM = 4
# sents_file = sys.argv[1]
sents_file = "tmp.csv"
dbpath = "new_words_detector.db"
# dbpath = sys.argv[2]
############################

def split_sents_file_into_small_chunkfiles(sents_fpath):
    tmp_dir = "tmp"
    if os.path.isdir(tmp_dir):
        os.system("rm -rf %s" % tmp_dir)
    os.mkdir(tmp_dir)
    
    num_lines = sum(1 for line in open(sents_fpath))
    chunk_size = int(num_lines / float(PARALLEL_NUM*10)) + 1 
    os.system("split -l %d %s %s/" %(chunk_size, sents_file, tmp_dir))
    
    chunk_fpaths = [os.path.join(tmp_dir, fname) for fname in os.listdir(tmp_dir) ]
        
    return chunk_fpaths

def init_zibook(dbpath):
    # 从sqlite中读取(汉字,频率）
    zibook = {}
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute("select * from zibook");
    rows = cursor.fetchall()
    for row in rows: 
        zibook[row[0]] = int(row[1])
    cursor.close()
    conn.close()
    return zibook

def init_new_word_table(dbpath):
    conn = sqlite3.connect("new_words_detector.db")
    cur = conn.cursor()
    cur.execute('drop table IF EXISTS new_word_book') 
    cur.execute("""CREATE TABLE IF NOT EXISTS new_word_book (
                    id INTEGER PRIMARY KEY,
                    word VARCHAR(8) NOT NULL,
                    freq float NOT NULL,
                    pmi float NOT NULL,
                    entropy float NOT NULL
                    )
                """)
    conn.commit()
    return


def process(fpath):
    zibook = init_zibook(dbpath)
    wordbook = {}
    for row in open(fpath):
        row = row.strip().decode("utf8")
        #解析文本，统计汉字频率，分词统计词频
        vtools.slice_word(row, stats, wordbook)
    
    new_words = []
    for k,word in wordbook.items():
        if word.get_freq() < stats.FREQ:  continue
        word.entropy = vtools.clac_entropy(word)
        word.pmi = vtools.clac_pmi(word, stats.N, wordbook,zibook)
        
        if not word.entropy: continue
        if not word.pmi:continue 
#         if word.entropy<stats.ENTROPY: continue
#         if word.pmi< stats.PMI:  continue
        
        new_words.append( (word.text,word.freq,word.pmi, word.entropy) )
    
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO new_word_book(word,freq,pmi,entropy) VALUES (?,?,?,?)", new_words )
    conn.commit()
    cursor.close()
    conn.close()
    
    print fpath, "is done!"
    return

if __name__ == "__main__":
    
    import datetime 
    print datetime.datetime.now()
    
    chunk_fpaths = split_sents_file_into_small_chunkfiles(sents_file)
    
    init_new_word_table(dbpath)
    
    pool = multiprocessing.Pool(PARALLEL_NUM)
    rel  = pool.map(process, chunk_fpaths)
    
    tmp_dir = "tmp"
    if os.path.isdir(tmp_dir):
        os.system("rm -rf %s" % tmp_dir)

    print datetime.datetime.now()



    


