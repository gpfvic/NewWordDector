time ./word2vec -train user_query.txt -output vectors_user_query.bin -cbow 1 -size 200 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 20 -binary 1 -iter 15

#./distance vectors.bin

#./compute-accuracy vectors.bin 30000 < questions-words.txt

#./word-analogy vectors.bin


# 分类
#time ./word2vec -train train_data.txt -output classes.txt -cbow 1 -size 200 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 20 -iter 15 -classes 20
#sort classes.txt -k 2 -n > classes.sorted.txt