import numpy as np
import pandas as pd
import pickle
import nltk
from data_view import view
from word2cloud import word2cloud
from word2num import Word2Num
from review2num import make_scores
from clean_data import clean_data
from export import export



if __name__ == "__main__":

	# product = view("./data/microwave.tsv")
	# product = view("./data_after_clean/microwave_clean.csv")
	product = pd.read_csv("./data_after_clean/microwave_clean.csv")
	# product = clean_data(product)
	num = product.shape[0]
	# print(product.columns)
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
	# sentence = product["review_body"][0]
	# print(sentence)
	# scores = make_scores(product[["review_id", "review_body"]])
	# scores = pd.read_csv('./run_data/microwave_scores.csv')
	# print(scores)
	# s = 0
	# for i in range(num):
	# 	if product.loc[i, "star_rating"] >= 4 and scores.loc[i, "score"] >= 0:
	# 		s += 1
	# 	elif product.loc[i, "star_rating"] <= 3 and scores.loc[i, "score"] < 0:
	# 		s += 1
	# print("accuracy:", s/num * 100)
	# y_label = export(product)
	# y_label = pd.read_csv("./ouput/microwave_export.csv")
	# print(y_label)
	# table = pd.merge(product, scores, on="review_id")
	# table = pd.merge(product, y_label, on="review_id")
	# table.to_csv("./ouput/all.csv")
	# print(table)
	#合并表

	# all_tabel = pd.DataFrame(columns=product.columns)
	# all_tabel['score'] = None
	# all_tabel['export'] = None
	# for i in range(num):
	# 	for c in product.columns:
	# 		all_tabel.loc[i, c] = product.loc[i, c]
	# 	all_tabel.loc[i, "score"] = scores.loc[i, "score"]
	# 	all_tabel.loc[i, "export"] = y_label.loc[i, "sale_count"]
	# 	print(i)
	# all_tabel.to_csv("./ouput/all.csv")
	all_tabel = pd.read_csv("./ouput/all.csv")
	print(all_tabel)







