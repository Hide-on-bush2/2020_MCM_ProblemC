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
from merge_data import merge_data




if __name__ == "__main__":
	product_name = "pacifier"
	# product = view("./data/" + product_name + ".tsv")
	product = pd.read_csv("./data_after_clean/" + product_name + "_clean.csv")

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

	scores = make_scores(product[["review_id", "review_body"]], product_name)
	# scores = pd.read_csv('./run_data/' + product_name + '_scores.csv')

	# s = 0
	# for i in range(num):
	# 	if product.loc[i, "star_rating"] >= 4 and scores.loc[i, "score"] >= 0:
	# 		s += 1
	# 	elif product.loc[i, "star_rating"] <= 3 and scores.loc[i, "score"] < 0:
	# 		s += 1
	# print("accuracy:", s/num * 100)

	y_label = export(product, product_name)
	# y_label = pd.read_csv("./ouput/" + product_name + "_export.csv")
	# print(y_label)

	#合并表
	all_tabel = merge_data(product, scores, y_label, product_name)
	# all_tabel = pd.read_csv("./ouput/" + product_name + "_all.csv")
	# print(all_tabel)

	#训练神经网络
	# data_set = pd.read_csv('./fitting_data/fitting_data.csv')
	# model = neural_network(data_set)
	# print(model.run([0.9, 5, 1]))
	







