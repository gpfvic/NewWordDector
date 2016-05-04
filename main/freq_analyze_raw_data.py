# -*- coding: utf-8 -*-  
'''
Created on 2016年1月12日

@author: gaopengfei
'''

import re,sqlite3
from tqdm import tqdm
from luigi import worker

# fpath = "tmall_product.csv"
# fpath = "dump.sql"
fpath = "OTC.txt"

count  = 0
def filter_unchinese(text):
    """过滤其它字符，只保留中文"""
    data = []
    global count
    for t in re.findall(ur'[\u4e00-\u9fff]+',text):
        data.append(t.strip())
    return data


wordbook = {}
for row in tqdm(open(fpath)):
    ts = filter_unchinese(row.strip().decode("utf8"))
    for t in ts:
        wordbook[t] = wordbook.get(t,0) + 1
    
with open("tmp.csv",'w') as f:    
    for k,v in wordbook.items():
        a = "%s,%d\n" % (k,v)
        f.write(a.encode("utf8"))

# 保存数据

conn = sqlite3.connect("new_words_detector.db")
cur = conn.cursor()
cur.execute('drop table IF EXISTS zibook') 
cur.execute("""CREATE TABLE IF NOT EXISTS word_freq_book (
                word VARCHAR(8) NOT NULL,
                freq int(11) NOT NULL,
                PRIMARY KEY('word')
                )
            """)

for word, freq in wordbook.items():
    try:
        cur.execute("INSERT INTO word_freq_book(word,freq) VALUES (?,?)", (word,freq) )
    except sqlite3.IntegrityError:
        print word, freq
conn.commit()

cur.close()
conn.close()



