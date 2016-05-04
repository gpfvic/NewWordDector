#coding:utf-8
'''
Created on 2015-8-12

@author: g00297221
'''
import math,sys
from Word import Word
import helper

import __builtin__

try:
    profile = __builtin__.__dict__['profile']
except KeyError:
    # No line profiler, provide a pass-through version
    def profile(func): return func
    __builtin__.profile = profile

def slice_word(text,stats,wordbook):
    """abcabc
        => Word:  abc        Freq:2        Left:  {'c': 1}        Right:  {'a': 1}
        => Word:abcab        Freq:1        Left:        {}        Right:  {'c': 1}
    """
    for i in range(len(text)):
        for j in range(i,len(text)):
            if i==j or j-i>=stats.D: continue
            w = text[i:j+1]
            try:
                wordbook[w]
            except KeyError:
                wordbook[w] = Word(w)
            wordbook[w].incr()
            #左邻字
            if i>0: wordbook[w].add_left(text[i-1])
            #友邻字
            if j<len(text)-1: wordbook[w].add_right(text[j+1]) 
    return

def predictate(word, stats, wordbook, zibook):
    word.entropy = clac_entropy(word)
    word.pmi = clac_pmi(word, stats.N, wordbook,zibook)
    if not word.entropy or not word.pmi  or word.entropy<stats.ENTROPY or word.pmi< stats.PMI:  
        return False
    return True


def clac_pmi(word,N,wordbook,zibook):
    """点互信息：取组合的最小值 p(abc)/[p(a)p(bc)]"""
    combs = get_combinations(word.text)
    probs = []
    for comb in combs:
        p = reduce(lambda x, y: x*y, [wordbook[w].get_freq() if w in wordbook.keys() else zibook[w] for w in comb])
        probs.append(float(wordbook[word.text].get_freq()*N)/(p+0.001))
    return evaluate(probs)

def clac_entropy(word):
    """自由度: 计算Word的左右信息熵，取较小值"""
    left_entr = Entropy(word.left)
    right_entr = Entropy(word.right)
    return min([left_entr,right_entr])


def format_dict(ddict):
    a = ""
    for k,word in ddict.items():
        a += "%s%s" % (k,word)
    return  "{%s}" % a
            
def evaluate(arr):
    # 凝固度 , 平均值
    tmp = filter(None, arr)
    if not tmp: return None 
    return sum(tmp) / float(len(tmp)) 



def Entropy(exr):
    if len(exr)<2: return 0.00001
    log_e = lambda x:math.log(x)
    infoc = 0
    textlen = sum(exr.values())
    for word in exr.values():
        freq = 1.0001 * word/textlen
        infoc += freq * log_e(freq)
    infoc *= -1
    return infoc


def get_combinations(text):
    """[['ab', 'c'], ['a', 'bc']]"""
    combinations = []
    arr = []
    slen = len(text)
    __find_factor(slen,slen,combinations,arr)
    
    elements = []
    for comb in combinations:
        tmp = [0] + comb
        elements.append([text[tmp[i]:tmp[i]+tmp[i+1]] for i in range(len(tmp)-1)])
    return elements

    

def __find_factor(ssum, n, combinations, arr):
    
    if n<0 or ssum<=0 or sum(arr)>ssum:
        return
    
    if ssum==2:
        combinations.append([1,1])
        return
    
    if sum(arr)==ssum:
        if  len(arr)==ssum or len(arr)==1:
            return
#         print "ssum:%d n:%d add:%d-> list: " % (ssum,n,sum(arr)), arr
        combinations.append(arr[:])
        return
    
    for t in range(1,n+1)[::-1]:
        arr.append(t)
        __find_factor(ssum, n-t, combinations, arr)
        arr.pop()
    return

