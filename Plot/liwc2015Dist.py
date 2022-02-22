#!../../anaconda2/bin/python

import pandas as pd
import numpy as np

data = pd.read_csv("LIWC2015_MJ.csv")

#print(data.head()) 
for col in data.columns.values.tolist():
	print(col)
	#print(list(data[col]))

#mean	
#for col in data.columns.values.tolist()[2:]:
#	print(np.mean(data[col]))
#	print(np.std(data[col]))
#median
for col in data.columns.values.tolist()[2:]:
	currentN = data[col].tolist()
	N = len(currentN)
	currentN.sort()
	if N % 2 ==0:
		median1 = currentN[N/2]
		median2 = currentN[N/2-1]
		median = (median1+median2)/2
		print(median)
	else:
		median = currentN[N/2]
		print(median)





