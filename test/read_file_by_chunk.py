#coding:utf-8
'''
Created on 2015年8月14日

@author: g00297221
'''
def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

i=0
f = open("..\\data\\xiyouji.txt")
for piece in read_in_chunks(f):
#     print piece
    i +=1
    print "-------------------------" , i