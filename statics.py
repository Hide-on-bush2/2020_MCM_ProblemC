import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
	product_name = "microwave"
	data = pd.read_csv("./data_after_clean/" + product_name + "_clean.csv")
	num = data.shape[0]
	# print(data)
	total_info = data.describe()
	# print(total_info)

	#star_rating的分布
	# star_counts = data.star_rating.value_counts()
	# star_counts.plot(kind='bar')
	# plt.title("star_rating counts")
	# plt.ylabel(u"rating counts")
	# plt.xlabel("rating level")
	# plt.savefig("./data_jpg/" + product_name + "/rating_counts.jpg")
	# plt.show()

	#对各种商品的分析
	parent_set = set(data["product_parent"])
	num_parent = len(parent_set)

	#每种产品收到的评论数
	num_review = {}
	for i in range(num):
		pdt = data.loc[i, "product_parent"]
		if pdt in num_review:
			num_review[pdt] += 1
		else:
			num_review[pdt] = 1
	num_review = sorted(num_review.items(), key=lambda x:-x[1])
	# print(list_review)
	x = [str(re[0]) for re in num_review[0:10]]
	y = [re[1] for re in num_review[0:10]]
	# print(x)
	# print(y)
	plt.figure(figsize=(12,4))
	plt.bar(x, y, width=0.8)
	plt.savefig('./data_jpg/' + product_name + '/review_nums.jpg')
	plt.show()
	


