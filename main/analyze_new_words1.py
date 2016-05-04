# -*- coding: utf-8 -*-  
'''
Created on 2016年1月11日

@author: gaopengfei
'''
import sqlite3

wordbook = {}
# 从sqlite中读取词库
dbpath="new_words_detector.db"

def dict_factory(cursor, row):
    d = {}
    # 遍历字段: id, word, freq, pmi, entropy
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    try:
        word = wordbook[d['word']]
        word = {
                    "freq": word["freq"] + d["freq"],
                    "pmi" : max(word['pmi'], d['pmi']),
                    "entropy" : max(word['entropy'], d['entropy']) 
                }
        wordbook[d['word']] = word
    except KeyError:
        wordbook[d['word']] = d
    return d

conn = sqlite3.connect(dbpath)
conn.row_factory = dict_factory
cursor = conn.cursor()
cursor.execute("select * from new_word_book");
rows = cursor.fetchall()
cursor.close()
conn.close()

# 合并

conn = sqlite3.connect("new_words_detector.db")
cursor = conn.cursor()
cursor.execute('drop table IF EXISTS merged_word_book') 
cursor.execute("""CREATE TABLE IF NOT EXISTS merged_word_book (
                id INTEGER PRIMARY KEY,
                word VARCHAR(8) NOT NULL,
                freq float NOT NULL,
                pmi float NOT NULL,
                entropy float NOT NULL
                )
            """)
conn.commit()

cursor.executemany("""INSERT INTO merged_word_book 
                    (word,freq,pmi,entropy)  
                    VALUES (?,?,?,?)""",  
                    [(k,w['freq'],w['pmi'],w['entropy'] ) for k,w in wordbook.items() ] )

conn.commit()
cursor.close()
conn.close()

