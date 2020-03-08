import pandas as pd
import numpy as np

def vote2num(data, product_name):
	vote_df = pd.DataFrame(columns=["vote_num"])
	num = data.shape[0]
	for i in range(num):
		vote_df.loc[i, "vote_num"] = 1 + data.loc[i, "helpful_votes"] / (data.loc[i, "total_votes"] + 1) * np.log10(data.loc[i, "total_votes"] + 1)
		print(i)
	vote_df.to_csv("./vote_data/" + product_name + "_vote.csv")
	return vote_df