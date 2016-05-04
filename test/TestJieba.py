# -*- coding: utf-8 -*-  
'''
Created on 2016年1月8日

@author: gaopengfei
'''
import jieba,random

jieba.set_dictionary("..\\main\\mydict_non_med.txt")

fpath = "..\\main\\sents.txt"


segs = jieba.lcut("杜蕾斯", HMM=False)
#上|海|玖|健|康复器|材|有限公司|
print "|".join(segs)

    