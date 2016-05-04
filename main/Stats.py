# coding:utf8
'''
Created on 2015年8月13日

@author: gaopengfei
'''
import ConfigParser

class Stats:
    ini_file = './config.ini'
    cf = ConfigParser.ConfigParser()
    
    def __init__(self):
        # config
        self.cf.read(self.ini_file)
        self.D = self.cf.getint("constant", "D")
        self.PMI = self.cf.getfloat("predicate", "PMI")
        self.ENTROPY = self.cf.getfloat("predicate", "ENTROPY")
        self.FREQ = self.cf.getint("predicate", "FREQ")
        self.N = self.cf.getint("running_time", "N")
        self.tFreq = self.cf.getint("filter", "tFreq")
        
    def set_pmi(self, value):
        self.__PMI = value

    def set_entropy(self, value):
        self.__ENTROPY = value

    def set_freq(self, value):
        self.__FREQ = value
        self.set_t_freq(value)

    def set_t_freq(self, value):
        self.__tFreq = value
     
    def set_D(self, D):
        self.D = D
        
    def set_N(self, N):
        self.N = N
        self.cf.set("running_time", "N", self.N)
        self.cf.write(open(self.ini_file, 'w'))  
        
    def add_N(self, N):
        self.N += N
        
