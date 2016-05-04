#coding:utf8
'''
Created on 2015年8月13日

@author: gaopengfei
'''
import copy
from functools import wraps
import time

def func_info(func):
    def _func_info(*args, **kwargs):
        print("entering %s" % func.__name__.upper())
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print("\tleaving %s, time: %.3f" % (func.__name__.upper(), end-start))
        return ret
    return _func_info



def filter_by_freq(wordbook,stats):
    """为了节省内存空间，删除频率低于阈值的Word对象"""
    words = copy.deepcopy(wordbook.keys())
    for w in words:
        word = wordbook[w]
        if word.get_freq()<stats.tFreq:
            wordbook.pop(w, None)
    return
