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
	all_tabel.to_csv("./ouput/" + product_name + "_all.csv")
	return all_tabel