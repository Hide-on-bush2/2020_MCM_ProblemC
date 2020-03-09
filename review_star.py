import pandas as pd
import numpy as np

def naive_bayes(data, product_name):
	num = data.shape[0]
	# words = ["great", "like", "well", "good"]
	words = ["stopped", "much", "disappoint", "disappointment", "enthusiastic", "expensive", "bad", "poor"]
	probability = {}
	for w in words:
		sum_review = 0
		sum_star = 0
		for i in range(num):
			if w in data.loc[i, "review_body"]:
				sum_review += 1
				if data.loc[i, "star_rating"] <= 3:
					sum_star += 1
			print(i)
		probability[w] = (sum_star, sum_review, sum_star / sum_review) 
	f = open("./problemE/" + product_name + "_negetive.txt", "w")
	for key, val in probability.items():
		f.write(key + " : " + str(val[0]) + ", " + str(val[1]) + " ," + str(val[2]) + "\n")
	f.close()

