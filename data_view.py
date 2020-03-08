import numpy as np
import pandas as pd
import re as re
import matplotlib.pyplot as plt
from word2cloud import word2cloud

def view(filename):
	if filename == "./data/pacifier.tsv":
		data = pd.read_csv("./data/pacifier2.tsv")
		return data
	data = pd.read_csv(filename, sep='\t')
	# print(dryer)
	information = data.describe()
	# print(information)
	
	return data

	# plt.show(wc)
