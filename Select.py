import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

if __name__ == "__main__":
	product_name = "hair_dryer"
	df = pd.read_csv("./all_data/" + product_name + "_all_three.csv")
	re = pd.DataFrame(columns=df.columns)
	num = df.shape[0]
	for i in range(num):
		if df.loc[i, "Total score5"] == "#VALUE!":
			continue
		if df.loc[i, "Total score5"] != " " and float(df.loc[i, "Total score5"]) > 0.65:
			re = re.append(df.loc[i], ignore_index=True)
		print(i)
	print(re)
	re.to_csv("./select/" + product_name + "_select5.csv")

	# re = pd.read_csv("./select/" + product_name + "_select.csv")
	product_class = re.product_parent.value_counts()
	dict_class = product_class[0:4].to_dict()

	f = open('./select/txt/' + product_name + '_parent5.txt', 'w')
	for key, val in dict_class.items():
		f.write(str(key) + ":" + str(val) + "\n")
	f.close()
	# x_ = [key for key in dict_class]
	# x = [str(key) for key in dict_class]
	# y = [val for key, val in dict_class.items()]

	# plt.figure(figsize=(12,4))
	# plt.bar(x, y)
	# plt.ylabel("quantity of sale")
	# plt.xlabel("product parent")
	# plt.savefig("./select/img/" + product_name + ".jpg")
	# plt.show()

	# title = {}
	# for parent in x_:
	# 	t = re[re["product_parent"] == parent]
	# 	title[(t["product_title"].values)[0]] = dict_class[parent]

	# print(pd.Series(title))
	# with open('./select/json/' + product_name + '.json','a') as outfile:
	#     json.dump(title,outfile,ensure_ascii=False)
	#     outfile.write('\n')
	# f = open('./select/txt/' + product_name + '.txt', 'w')
	# f.write(str(title))
	# for key, val in title.items():
	# 	f.write(key + ":" + str(val) + "\n")
	# f.close()
