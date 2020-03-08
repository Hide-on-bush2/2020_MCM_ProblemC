import numpy as np
import pandas as pd
import pickle
import nltk
from data_view import view
from word2cloud import word2cloud
from word2num import Word2Num
from review2num import make_scores
from clean_data import clean_data, pacifier_clean, try_run
from export import export
from neural_network import neural_network
import tensorflow as tf
from merge_data import merge_data, merge_value
from vote2num import vote2num
from entropy import get_entropy



if __name__ == "__main__":
	product_name = "microwave"
	# product = view("./data/" + product_name + ".tsv")
	# product = pd.read_csv("./data_after_clean/" + product_name + "_clean.csv")

	# product = pacifier_clean("./data/pacifier.tsv")
	# product = clean_data(product, product_name)
	# product = pd.read_csv("./data/pacifier.tsv", sep='\t')
	# product = try_run(product, 3457, 10000)

	# num = product.shape[0]
	# word2cloud(text)
	# num_word = Word2Num(dryer["review_body"])

	# classifier_f = open("./bayes_model/naivebayes.pickle", "rb")
	# classifier = pickle.load(classifier_f)
	# classifier_f.close()
	# classifier.show_most_informative_features(30)
	# class_ = classifier.prob_classify({"good":True})
	# print(class_.prob(1), class_.prob(0))

	# scores = make_scores(product[["review_id", "review_body"]], product_name)
	# print(scores)
	# scores = pd.read_csv('./run_data/' + product_name + 'new_scores.csv')

	# s = 0
	# for i in range(num):
	# 	if product.loc[i, "star_rating"] >= 4 and scores.loc[i, "score"] >= 0:
	# 		s += 1
	# 	elif product.loc[i, "star_rating"] <= 3 and scores.loc[i, "score"] < 0:
	# 		s += 1
	# 	print(i)
	# print("accuracy:", s/num * 100)

	## 计算好的误判比率
	# good_star = 0
	# good_false = 0
	# for i in range(num):
	# 	if product.loc[i, "star_rating"] >= 4:
	# 		good_star += 1
	# 		if scores.loc[i, "score"] < 0:
	# 			good_false += 1
	# 	print(i)
	# #计算坏的误判概率
	# bad_star = 0
	# bad_false = 0
	# for i in range(num):
	# 	if product.loc[i, "star_rating"] <= 3:
	# 		bad_star += 1
	# 		if scores.loc[i, "score"] > 0:
	# 			bad_false += 1
	# 	print(i)
	# print("good_false:", good_false / good_star * 100)
	# print("bad_false:", bad_false / bad_star * 100)

	# y_label = export(product, product_name)
	# y_label = pd.read_csv("./ouput/" + product_name + "_export.csv")
	# print(y_label)

	#合并表
	# all_tabel = merge_data(product, scores, y_label, product_name)
	# all_tabel = pd.read_csv("./ouput/" + product_name + "_all.csv")
	# print(all_tabel)

	#训练神经网络
	# data_set = pd.read_csv('./fitting_data/fitting_data.csv')
	# model = neural_network(data_set)
	# print(model.run([0.9, 5, 1]))

	#投票量化
	# votes = vote2num(all_tabel, product_name)
	# votes = pd.read_csv("./vote_data/" + product_name + "_vote.csv")
	# print(votes)

	#将标星，投票量化，评论量化，销售量做表
	# value_data = merge_value(all_tabel, scores, y_label, votes, product_name)
	value_data = pd.read_csv("./value_data/" + product_name + "_value.csv")
	# print(value_data)

	#测试信息熵
	print("star_rating:")
	print(get_entropy(value_data["star_rating"], "star_rating"))
	print("helpful_votes")
	print(get_entropy(value_data["vote_values"], "helpful_votes"))
	print("review_scores")
	print(get_entropy(value_data["review_scores"], "review_score"))
	







