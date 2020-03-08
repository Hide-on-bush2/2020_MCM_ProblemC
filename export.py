import pandas as pd
import numpy as np
import datetime as dt

def get_date(str):
	month = ""
	i = 0
	while i < len(str) and str[i] != '/':
		month += str[i]
		i += 1
	date = ""
	i += 1
	while i < len(str) and str[i] != '/':
		date += str[i]
		i += 1
	year = ""
	i += 1
	while i < len(str):
		year += str[i]
		i += 1
	return int(year), int(month), int(date)

def between_date(start_date, end_date, curr_date):
	return curr_date >= start_date and curr_date <= end_date

def puple2date(t):
	return dt.datetime(t[0], t[1], t[2], 0)

def count_sale(data, start_date, end_date, product_parent, i):
	s = 0
	for j in range(i)[: : -1]:
		curr_date = puple2date(get_date(data.loc[j, "review_date"]))
		if between_date(start_date, end_date, curr_date):
			if data.loc[j, "product_parent"] == product_parent:
				s += 1
		else:
			break
	return s



def export(data, product_name):
	# print(data["review_date"][0])
	# print(puple2date(get_date(data["review_date"][0])))
	start = 0
	end = 0
	if product_name == "hair_dryer":
		start = 361
		end = 9587
	elif product_name == "microwave":
		start = 100
		end = 822
	else:
		start = 668
		end = 15978
	delta = dt.timedelta(weeks=4)
	sale = pd.DataFrame(columns=["review_id", "sale_count"])
	num = data.shape[0]
	for i in range(data.shape[0]):#从2013年开始
		pro_par = data.loc[i, "product_parent"]
		curr_date = puple2date(get_date(data.loc[i, "review_date"]))
		# sale.loc[i, "sale_count"] = count_sale(data, curr_date, curr_date + delta, pro_par, i)
		# sale.loc[i, "review_id"] = data.loc[i, "review_id"]
		if i < start:
			sale.loc[i, "sale_count"] = float('nan')
			sale.loc[i, "review_id"] = data.loc[i, "review_id"]
		elif i >= end:
			sale.loc[i, "sale_count"] = float('nan')
			sale.loc[i, "review_id"] = data.loc[i, "review_id"]
		else:
			sale.loc[i, "sale_count"] = count_sale(data, curr_date, curr_date + delta, pro_par, i)
			sale.loc[i, "review_id"] = data.loc[i, "review_id"]
		print(i)
	print(sale)
	location = "./ouput/" + product_name + "_export.csv"
	sale.to_csv(location)
	return sale






