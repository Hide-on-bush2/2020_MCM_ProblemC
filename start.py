import numpy as np
import pandas as pd
import pickle
import nltk
from data_view import view
from word2cloud import word2cloud
from word2num import Word2Num
from review2num import make_scores



if __name__ == "__main__":

	product = view("./data/microwave.tsv")
	num = product.shape[0]
	# print(dryer)

	# text = ""
	# for sentence in dryer["review_body"]:
	# 	text += sentence


	# word2cloud(text)
	# num_word = Word2Num(dryer["review_body"])
	# classifier_f = open("./bayes_model/naivebayes.pickle", "rb")
	# classifier = pickle.load(classifier_f)
	# classifier_f.close()

	# classifier.show_most_informative_features(30)
	# class_ = classifier.prob_classify({"good":True})
	# print(class_.prob(1), class_.prob(0))
	sentence = product["review_body"][0]
	print(sentence)
	# scores = make_scores(product["review_body"])
	scores = pd.read_csv('./run_data/microwave_scores.csv')
	s = 0
	for i in range(num):
		if product.loc[i, "star_rating"] >= 4 and scores.loc[i, "score"] >= 0:
			s += 1
		elif product.loc[i, "star_rating"] <= 3 and scores.loc[i, "score"] < 0:
			s += 1
	print("accuracy:", s/num * 100)
