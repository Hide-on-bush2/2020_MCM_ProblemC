#将review向量化
import nltk
import random
import pickle
import numpy as np
import pandas as pd
from split_word import split_word

def load_dataset(filename):
	data_set = pd.read_table(filename, names=["reviews", "label"])
	return data_set

def Word2Num(document):
	train_set = load_dataset("./review_dataset/amazon_cells_labelled.txt")
	num = train_set.shape[0]
	print(num)
	# print(train_set)
	# print(document)
	# document = [train_set["reviews"].values, train_set["label"].values]
	document = [(train_set.loc[i, "reviews"], train_set.loc[i, "label"]) for i in range(num)]
	# print(document)
	random.shuffle(document)

	text = ""
	for sentence in train_set["reviews"]:
		text += sentence
	# print(text)
	# pattern1 = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') #匹配标点符号的正则表达式
	# pattern2 = re.compile(r'<br />') #匹配一些无用符号的正则表达式
	# pattern3 = re.compile('<BR>')
	# text = re.sub(pattern1, '', text)
	# text = re.sub(pattern2, ' ', text)
	# text = re.sub(pattern3, ' ', text)
	# # print(text)

	# seg_list_exact = jieba.cut(text, cut_all = False) # 精确模式分词
	# # print(seg_list_exact)
	# all_words = []
	# remove_words = [' ', ',', '!', "'"]#去除词库
	# for word in seg_list_exact: # 循环读出每个分词
	# 	if word not in remove_words:
	# 		all_words.append(word) # 分词追加到列表
	# # print(all_words)
	all_words = split_word(text)
	all_words = nltk.FreqDist(all_words)
	# print(all_words.most_common(15))
	# print(all_words["good"])

	word_featrues = list(all_words.keys())[:3000]

	def find_features(sentence):
		# words = set(document)
		# print(words)
		featrues = {}
		for w in word_featrues:
			featrues[w] = (w in sentence)
		return featrues

	featruesets = [(find_features(rev), label) for (rev, label) in document]
	# print(featruesets)

	#贝叶斯分类器
	training_set = featruesets[:]
	# testing_set = featruesets[500:]

	classifier = nltk.NaiveBayesClassifier.train(training_set)
	classifier.show_most_informative_features(30)

	save_classifier = open("./bayes_model/naivebayes.pickle", "wb")
	pickle.dump(classifier, save_classifier)
	save_classifier.close()

















