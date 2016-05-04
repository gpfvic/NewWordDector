# -*- coding: utf-8 -*-  
'''
Created on 2016年1月12日

@author: gaopengfei
'''

import jieba

jieba.set_dictionary("address.txt1")
jieba.initialize()

data = []
for row in open("len4freq10.csv"):
    w,freq = row.decode("utf8").strip().split(",")
#     ts  = jieba.lcut(w,cut_all=False, HMM=False)
    ts  = jieba.cut(w,cut_all=False, HMM=False)
    num = sum([1 if len(t)>1 else 0 for t in ts])
    if num >0  : continue
    data.append((w,int(freq)))

data = sorted(data, key=lambda x : x[1], reverse=True)  
with open('words_20160112.csv', 'w') as f:
    f.write("\n".join(["%s,%d" %(w,f) for w,f in data]).encode("utf8"))



    