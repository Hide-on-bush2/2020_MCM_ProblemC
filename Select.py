import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

if __name__ == "__main__":
	product_name = "pacifier"
	df = pd.read_csv("./all_data/" + product_name + "_all.csv")
	re = pd.DataFrame(columns=df.columns)
	num = df.shape[0]
	for i in range(num):
		if df.loc[i, "Total score"] != " " and float(df.loc[i, "Total score"]) > 0.65:
			re = re.append(df.loc[i], ignore_index=True)
		print(i)
	print(re)
	re.to_csv("./select/" + product_name + "_select.csv")

	# re = pd.read_csv("./select/" + product_name + "_select.csv")
	product_class = re.product_parent.value_counts()
	dict_class = product_class[0:10].to_dict()
	x_ = [key for key in dict_class]
	x = [str(key) for key in dict_class]
	y = [val for key, val in dict_class.items()]

	plt.figure(figsize=(12,4))
	plt.bar(x, y)
	plt.ylabel("quantity of sale")
	plt.xlabel("product parent")
	plt.savefig("./select/img/" + product_name + ".jpg")
	plt.show()

	title = {}
	for parent in x_:
		t = re[re["product_parent"] == parent]
		title[(t["product_title"].values)[0]] = dict_class[parent]

	print(pd.Series(title))
	# with open('./select/json/' + product_name + '.json','a') as outfile:
	#     json.dump(title,outfile,ensure_ascii=False)
	#     outfile.write('\n')
	f = open('./select/txt/' + product_name + '.txt', 'w')
	# f.write(str(title))
	for key, val in title.items():
		f.write(key + ":" + str(val) + "\n")
	f.close()

