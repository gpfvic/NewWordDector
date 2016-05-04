# -*- coding: utf-8 -*-  
'''
Created on 2016年1月8日

@author: gaopengfei
'''

import sqlite3

conn = sqlite3.connect('D:\\data\\search_result\\search_query.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS query_log (
                id INT NOT NULL,
                time TEXT,
                source TEXT,
                merchant TEXT,
                user_query TEXT,
                fact_query TEXT,
                match_result INT,
                recommend_result INT,
                page INT,
                user_id TEXT,
                cost INT,
                memo TEXT, 
                PRIMARY KEY('id')
                )
            """)

fpath = 'D:\\data\\search_result\\aaa.csv'
for row in open(fpath):
    try:
        cur.execute('INSERT INTO query_log( \
                    id,time,source,merchant,user_query,\
                    fact_query,match_result,recommend_result,\
                    page,user_id,cost,memo)   \
                    VALUES ( ' +  row.strip() +')')
    except sqlite3.OperationalError:
        print row


conn.commit()


cur.close()
conn.close()



