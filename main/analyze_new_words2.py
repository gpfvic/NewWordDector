# -*- coding: utf-8 -*-  
'''
Created on 2016年1月11日

@author: gaopengfei
'''

import sqlite3
import fuzzywuzzy
from tqdm import tqdm 

def dict_factory(cursor, row):
    d = {}
    # 遍历字段: id, word, freq, pmi, entropy
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    try:
        kw = d['word']
        word = wordbook[kw]
        word = {
                    "freq": word["freq"] + d["freq"],
                    "pmi" : max(word['pmi'], d['pmi']),
                    "entropy" : max(word['entropy'], d['entropy']) 
                }
        wordbook[kw] = word
    except KeyError:
        wordbook[kw] = d
    return d

####################################
wordbook = {}
# 从sqlite中读取词库
dbpath="new_words_detector.db"
conn = sqlite3.connect(dbpath)
conn.row_factory = dict_factory
cursor = conn.cursor()
cursor.execute("""
                select * 
                from merged_word_book 
                where freq > 10 and pmi > 20
                order by freq desc
                """);
rows = cursor.fetchall()
cursor.close()
conn.close()
# 找出相似的字符串
word_set = set(wordbook.keys())

################################
### 成词条件

FINAL_WORDS = set()
##1 取entropy大于0.1

conn = sqlite3.connect(dbpath)
conn.row_factory = dict_factory
cursor = conn.cursor()
cursor.execute("""
                select * 
                from merged_word_book 
                where freq > 10 and pmi > 20 and entropy >0.1
                order by freq desc
                """);
rows = cursor.fetchall()
# for d in rows:  FINAL_WORDS.add(d['word'])
cursor.close()
conn.close()


##2 识别相似字符串 ，频率相同，或相差5%以内， 取pmi大5倍以上的
choices = word_set.copy()

for w in tqdm(word_set):
    score_list = []
    for b in choices:
        ratio = fuzzywuzzy.ratio(w, b)
        if ratio > 0.6:
            score_list.append((b, ratio))
    score_list.sort(key=lambda i:i[1], reverse=True)
    
    if len(score_list)<1: continue
    word = wordbook[w]
    
    likely_word = {}
    for sw, _ in score_list:
        sword = wordbook[sw]
        dratio = sword['pmi'] / float(word['pmi']) 
        likely_word[dratio] = sw
    if len(likely_word)==0:
        FINAL_WORDS.add(w)
    else:
        most_likely_word = likely_word[ max(likely_word.keys()) ]
        FINAL_WORDS.add(most_likely_word)
    
# 保存最终数据结果
with open('final_words.csv', 'w') as f:
    for fw in FINAL_WORDS:
        fword = wordbook[fw]
        out = "%s,%d,%.2f,%.2f\n" % (fw, fword['freq'], fword['pmi'],fword['entropy'])
        f.write(out.encode("utf8"))

conn = sqlite3.connect("new_words_detector.db")
cursor = conn.cursor()
cursor.execute('drop table IF EXISTS final_words') 
cursor.execute("""CREATE TABLE IF NOT EXISTS final_words (
                id INTEGER PRIMARY KEY,
                word VARCHAR(8) NOT NULL,
                freq float NOT NULL,
                pmi float NOT NULL,
                entropy float NOT NULL
                )
            """)
conn.commit()

data = []
for w in FINAL_WORDS:
    word = wordbook[w]
    data.append( (w,word['freq'],word['pmi'],word['entropy'] ) )

cursor.executemany("""INSERT INTO final_words 
                    (word,freq,pmi,entropy)  
                    VALUES (?,?,?,?)""",  
                    data)
conn.commit()
cursor.close()
conn.close()
    



