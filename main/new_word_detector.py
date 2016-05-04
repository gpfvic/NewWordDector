#coding:utf-8
import sys
import vio, vtools, Stats
from helper import func_info


# global variables
stats = Stats.Stats()
wordbook = {}
zibook = {}
new_words = []

@func_info
def init(args):
	"""初始化全局参数"""
	global wordbook, zibook
	del wordbook; wordbook={}
	del zibook;zibook={}
	if not args.D: stats.set_D(args.D)
	if not args.pmi: stats.set_pmi(args.pmi)
	if not args.entropy: stats.set_entropy(args.entropy)
	if not args.freq: stats.set_freq(args.freq)
	return

@func_info
def preprocess(fpath):
	data, N = vio.readFile(fpath)
	stats.set_N(N)
	N_processed=0
	for row in data:
		vtools.slice_word(row, stats, wordbook, zibook)
		N_processed += len(row)
	return


@func_info
def calc_filter_words():
	print "Start filtering ..."
	for k,word in wordbook.items():
		if word.get_freq()>stats.FREQ and word.predictate(stats, wordbook, zibook):
			new_words.append("%s,%s,%.2f,%.2f" % (word.text,word.freq,word.sol,word.entropy))
	return 

@func_info
def save_result(dpath, save_fpath):
	print "Start Saving ..."
	with open(save_fpath,'w') as f:
		f.write("\n".join(new_words).encode("utf-8"))
	return


@func_info	
def run(args):
	if not args.data_file or not args.save_file:
		sys.exit("File path error!")
		
	data_fpath = args.data_file
	save_fpath = args.save_fpath
	
	# step 1 : 读文本数据
	global new_words
	init(args)
	
	preprocess(data_fpath)
	
	calc_filter_words()
	
	del new_words; new_words=[]
 	save_result(save_fpath)
	print "%s DONE!" % save_fpath
	return





