# 读取文件，过滤掉非中文字符
SENTS_FILTERED_UNCHINESE = OTC1.txt
GEN_WORDS_AND_COUNTING = words_stats.csv
SQLITE_DB = new_words_detector.db
DICT_FOR_FILTERING = D:\\data\\dict\\mydict_non_med.txt

# 统计句子
$(SQLITE_DB):
	@python  freq_analyze_raw_data.py $(SENTS_FILTERED_UNCHINESE)


#从句子生成词
$(GEN_WORDS_AND_COUNTING) : $(SENTS_FILTERED_UNCHINESE) 
	@echo %Date:~0,4%%Date:~5,2%%Date:~8,2%%Time:~0,2%%Time:~3,2%%Time:~6,2%
	@echo "#2. 生成词语，并统计"
	@python gen_words_and_stats.py $(SENTS_FILTERED_UNCHINESE)  $(GEN_WORDS_AND_COUNTING)

$(SENTS_FILTERED_UNCHINESE) :
	@echo %Date:~0,4%%Date:~5,2%%Date:~8,2%%Time:~0,2%%Time:~3,2%%Time:~6,2% 
	@echo "#1. 解析文本，保留中文句子"
	@python read_data.py $(SENTS_FILTERED_UNCHINESE) $(SQLITE_DB)
	

clean:
	rm $(SENTS_FILTERED_UNCHINESE) $(GEN_WORDS_AND_COUNTING)