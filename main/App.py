#coding:utf-8

import argparse


def parse_args():
	parser = argparse.ArgumentParser(
		description='New Word Detector', 
		epilog='Use %(prog)s {command} -h to get help on individual commands'
	)

	parser.add_argument("--data_file", dest="data_file", help="raw data files")
	parser.add_argument("-D", type=int, dest="D", help="max length of word")
	parser.add_argument("-pmi",type=float, help="pmi")
	parser.add_argument("-entropy",type=float, help="entropy")
	parser.add_argument("-freq", type=int, help="frequency")

	return parser.parse_args()


if __name__=="__main__":
	args = parse_args()
	