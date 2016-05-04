#coding:utf8
'''
Created on 2015年1月5日

@author: gaopengfei
'''
import logging

class vLogger:

    def __init__(self, logname):
        self.logger = logging.getLogger(logname)
        self.logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(logname+".log")
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # add the handlers to self.logger
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)
        return
    def debug(self,info):
        self.logger.debug(info)
        
    def warn(self,info):
        self.logger.warn(info)
        
    def info(self,info):
        self.logger.info(info)
    
    def error(self,info):
        self.logger.error("error message")

