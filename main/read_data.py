# -*- coding: utf-8 -*-  
'''
Created on 2016年1月7日

@author: gaopengfei
'''
import re,sys, sqlite3, jieba, datetime
from collections import Counter
import Stats


def count_zi_stats(text):
    word_freq_list = Counter(text).most_common()
    for z,n in word_freq_list:
        zibook[z] = zibook.get(z,0) + n
    return

def filter_unchinese(text):
    """过滤其它字符，只保留中文"""
    data = []
    for ts in re.findall(ur'[\u4e00-\u9fff]+',text):
        count_zi_stats(ts.strip())
        data.append(ts.strip())
    return data

def filter_word_by_jieba(text):
    """利用分词过滤常用词，例如语气词等"""
    tmp_segs = jieba.lcut(text, cut_all=False, HMM=False)
    
    ssegs,tmp = [],[]
    for seg in tmp_segs:
        if seg == ".":
            ssegs.append(tmp)
            tmp = []
        else:
            tmp.append(seg)
    
    data = []
    
    def part_by_part(segs):
        tmp = ""
        for idx, seg in enumerate(segs):
            if len(seg)==1: tmp += seg
            if (idx==len(segs)-1 or len(segs[idx+1])>1) and len(tmp)>1:
                data.append(tmp)
                tmp = ""
    for ss in ssegs:
        part_by_part(ss)
    
    return data

########################################

print datetime.datetime.now()

stats = Stats.Stats()
zibook = {}
fpath = "sample.csv"

jieba.set_dictionary("mydict_non_med.txt")



data = []
N = 0
for idx,line in enumerate(open(fpath)):
    try:
        row = line.decode("gb2312").strip()
    except UnicodeDecodeError:
        row = line.decode("utf8").strip()
    if not row:    continue 
    
    txts = filter_unchinese(row)
    # 合并短文本并用.做分割符，加快分词
    merged_txts = ".".join(txts)
    segs = filter_word_by_jieba(merged_txts)
    
    data = data + segs
    
    if idx%1000==0: 
        print idx    
        
    
data = filter(lambda x:x!="" and len(x)>1, data)
N = len("".join(data))


stats.set_N(N)

#将解析的句子保存到本地文件
ofile = "sents.txt"
with open(ofile,'w') as f:
    f.write("\n".join(data).encode("utf8"))

# 将zibook保存到sqlite中
conn = sqlite3.connect("new_words_detector.db")
cur = conn.cursor()
cur.execute('drop table IF EXISTS zibook') 
cur.execute("""CREATE TABLE IF NOT EXISTS zibook (
                zi VARCHAR(8) NOT NULL,
                freq int(11) NOT NULL,
                PRIMARY KEY('zi')
                )
            """)
cur.executemany("INSERT INTO zibook(zi,freq) VALUES (?,?)", [(zi,freq) for zi,freq in zibook.items()] )
conn.commit()

cur.close()
conn.close()

print datetime.datetime.now()


