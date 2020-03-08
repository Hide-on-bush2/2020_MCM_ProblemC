import numpy as np
import pandas as pd

def merge_data(product, scores, y_label, product_name):
	all_tabel = pd.DataFrame(columns=product.columns)
	all_tabel['score'] = None
	all_tabel['export'] = None
	for i in range(product.shape[0]):
		for c in product.columns:
			all_tabel.loc[i, c] = product.loc[i, c]
		all_tabel.loc[i, "score"] = scores.loc[i, "score"]
		all_tabel.loc[i, "export"] = y_label.loc[i, "sale_count"]
		print(i)
	#删除score为nan的
	all_tabel = all_tabel[all_tabel["score"] != float('nan')]
	all_tabel.index=range(len(all_tabel))
	all_tabel.to_csv("./ouput/" + product_name + "_all.csv")
	return all_tabel

def merge_value(product, scores, ylabel, votes, product_name):
	values = pd.DataFrame(columns=["star_rating", "review_scores", "vote_values", "export"])
	num = product.shape[0]
	for i in range(num):
		values.loc[i, "star_rating"] = product.loc[i, "star_rating"]
		values.loc[i, "review_scores"] = scores.loc[i, "score"]
		values.loc[i, "vote_values"] = votes.loc[i, "vote_num"]
		values.loc[i, "export"] = ylabel.loc[i, "sale_count"]
		print(i)
	values.to_csv("./value_data/" + product_name + "_value.csv")
	return values