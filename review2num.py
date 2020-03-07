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
	lam = lambda x : np.abs(x)
	return max(word_score, key=lam)


def make_scores(reviews):
	scores = pd.DataFrame(columns=["score"])
	num = reviews.shape[0]
	for i in range(num):
		scores.loc[i, "score"] = Review2Num(reviews[i])
		print(i)
	print(scores)
	scores.to_csv("./run_data/microwave_scores.csv")
	print("max:", max(scores["score"]))
	print("min:", min(scores["score"]))
	return scores