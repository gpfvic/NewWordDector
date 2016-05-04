# -*- coding: utf-8 -*-  
'''
Created on 2016年1月19日

@author: gaopengfei
'''
import re,jieba

fname = "tmall_product.csv"

def filter_unchinese(text):
    """过滤其它字符，只保留中文"""
    data = []
    for ts in re.findall(ur'[\u4e00-\u9fff]+',text):
        data.append(ts.strip())
    return data




