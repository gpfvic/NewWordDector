# -*- coding: utf-8 -*-  
'''
Created on 2016年1月12日

@author: gaopengfei
'''
import re
import jieba
from tqdm import tqdm 


#####加载词库




######
data = []
fname = "only_user_query.txt"
for i,row in enumerate(open(fname)):
    row = row.decode("utf8").strip()
#     rs = jieba.lcut(row)
    rs = jieba.cut(row)
    data.append(" ".join(rs).encode("utf8"))
    if i%10000: print "|".join(rs)
    
with open("user_query.txt", 'w') as f:
    f.write("\n".join(data))