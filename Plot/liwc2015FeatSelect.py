#!../../anaconda2/bin/python

import pandas as pd
import numpy as np

dataMJ = pd.read_csv("LIWC2015_MJ.csv")
dataTobacco = pd.read_csv("LIWC2015_tobacco.csv",index_col ="Filename")
dataVaping = pd.read_csv("LIWC2015_vaping.csv")
dataCessation = pd.read_csv("LIWC2015_cessation.csv")

featureVecList = []
labelList = []
for vec in dataTobacco[0:].values:
	if len(vec) ==94:
		featureVecList.append(np.array(vec.tolist()))
		labelList.append('tobacco')
	elif len(vec) ==95:
		featureVecList.append(np.array(vec.tolist()[1:]) )
		labelList.append('tobacco')
for vec in dataMJ[0:].values:
	if len(vec) ==94:
		featureVecList.append(np.array(vec.tolist()))
		labelList.append('MJ')
	elif len(vec) ==95:
		featureVecList.append(np.array(vec.tolist()[1:]) )
		labelList.append('MJ')
for vec in dataVaping[0:].values:
	if len(vec) ==94:
		featureVecList.append(np.array(vec.tolist()))
		labelList.append('vaping')
	elif len(vec) ==95:
		featureVecList.append(np.array(vec.tolist()[1:]) )
		labelList.append('vaping')
for vec in dataCessation[0:].values:
	if len(vec) ==94:
		featureVecList.append(np.array(vec.tolist()))
		labelList.append('cessation')
	elif len(vec) ==95:
		featureVecList.append(np.array(vec.tolist()[1:]) )
		labelList.append('cessation')

print('FINISH VECTORS AND LABELS')

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

featureList = dataMJ.columns.values.tolist()
print(featureVecList[0])

#vecList = featureVecList[0:2]
#print(vecList)
#print(np.array(vecList).shape)
#arrayFeature =np.stack(featureVecList, axis=0)
arrayFeature = np.array(featureVecList)
arrayLabel = np.array(labelList)
#print(95len(featureList),94len(featureVecList[0]))
print(arrayFeature.shape)

fitFeatureObj = SelectKBest(chi2, k=10).fit(np.nan_to_num(featureVecList), labelList)
for f in featureList:
	print(f)
for s in fitFeatureObj.scores_:
	print(s)





