import numpy as np
import pandas as pd

def clean_data(data):
	#删除没有买在这BB的那些评论者
	data = data[(data["verified_purchase"] == 'Y') | (data["vine"] == "Y") | (data["verified_purchase"] == 'y') | (data["vine"] == "y")]
	#删除marktetplace和product_category列
	data = data.drop(columns=["marketplace", "product_category"])
	#重新排列index
	data.index=range(len(data))
	print(data)
	data.to_csv("./data_after_clean/microwave_clean.csv")
	return data