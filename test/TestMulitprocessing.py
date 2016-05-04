# -*- coding: utf-8 -*-  
'''
Created on 2016年1月10日

@author: gaopengfei
'''

import multiprocessing as mul
import random ,time

def f(x):
    time.sleep(random.randint(0,3))
    print x
    return x**2

if __name__ == "__main__":
    pool = mul.Pool(5)
    rel  = pool.map(f,[1,2,3,4,5,6,7,8,9,10])
    print(rel)