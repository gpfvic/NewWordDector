#coding:utf-8
import os,re,sys

def filesIterator(dpath):
	files = [os.path.join(dpath,f) for f in os.listdir(dpath) if os.path.isfile(os.path.join(dpath,f))]
	return iter(files)

def readFile(fpath):
	data = []
	N = 0
	for line in open(fpath):
		try:
			row = line.decode("gb2312").strip()
		except UnicodeDecodeError:
			row = line.decode("utf8").strip()
		if not row:	continue
		txts = filter_unchinese(row)
		data = data + txts
	data = filter(lambda x: len(x)>1, data)
	N = len("".join(data))
	return data, N


def filter_unchinese(text):
	"""过滤其它字符，只保留中文"""
	data = []
	for ts in re.findall(ur'[\u4e00-\u9fff]+',text):
		data.append(ts.strip())
	return data
