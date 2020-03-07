import numpy as np
import pandas as pd
import re as re
import matplotlib.pyplot as plt
from word2cloud import word2cloud

def view(filename):
	dryer = pd.read_csv(filename, sep='\t')
	# print(dryer)
	information = dryer.describe()
	# print(information)
	
	return dryer

	# plt.show(wc)
