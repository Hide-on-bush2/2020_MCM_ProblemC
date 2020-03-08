import numpy as np
import pandas as pd

def clean_data(data, product_name):
	#删除没有买在这BB的那些评论者
	data = data[(data["verified_purchase"] == 'Y') | (data["vine"] == "Y") | (data["verified_purchase"] == 'y') | (data["vine"] == "y")]
	#删除marktetplace和product_category列
	data = data.drop(columns=["marketplace", "product_category"])
	#重新排列index
	data.index=range(len(data))
	location = "./data_after_clean/" + product_name + "_clean.csv"
	data.to_csv(location)
	return data

def pacifier_clean(filename):
	data = pd.read_csv(filename, sep='\t')
	data1 = data[0:950]
	data2 = data[951:3456]
	data3 = data[3457:]
	cleaned_data = data1.append(data2, ignore_index=True)
	cleaned_data = cleaned_data.append(data3, ignore_index=True)
	cleaned_data.to_csv("./data/pacifier2.tsv")
	return cleaned_data

def try_run(data, start, end):#0-880 883-3177 3178-end
	data = data[start:end]
	data.index=range(len(data))
	return data
