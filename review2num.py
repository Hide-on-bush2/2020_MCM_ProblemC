import numpy as np
import pandas as pd
import nltk
import pickle
from split_word import split_word

# def softmax(l):
# 	denominator = sum(np.exp(l))
# 	return [np.exp(x)/denominator for x in l]

def Review2Num(review):
	classifier_f = open("./bayes_model/naivebayes.pickle", "rb")
	classifier = pickle.load(classifier_f)
	classifier_f.close()
	review = split_word(review)
	# print(review)
	word_score = []
	for word in review:
		class_ = classifier.prob_classify({word:True})
		pro = class_.prob(1)
		if pro >= 0.5:
			word_score.append(pro)
		else:
			word_score.append(-(1 - pro))
		# word_score.append(pro)
	# print(word_score)
	# softmax_word = softmax(word_score)	
	# print(softmax_word)
	# lam = lambda x : -np.abs(x)
	# if len(word_score) == 0:
	# 	return 0
	# return max(word_score, key=lam)
	# word_score = sorted(word_score, key=lam)
	res = sum(word_score)
	if res > 120:
		return float('nan')
	return np.log(res + 26) - np.log(26)


def make_scores(reviews, product_name):
	scores = pd.DataFrame(columns=["review_id", "score"])
	num = reviews.shape[0]
	for i in range(num):
		scores.loc[i, "score"] = Review2Num(reviews.loc[i, "review_body"])
		scores.loc[i, "review_id"] = reviews.loc[i, "review_id"]
		print(i)
	print(scores)
	location = "./run_data/" + product_name + "_scores.csv"
	scores.to_csv(location)
	print("max:", max(scores["score"]))
	print("min:", min(scores["score"]))
	return scores