#!../../anaconda2/bin/python


#import os
#import shutil
#import random
import re
#import json
import pickle
import reader
import RegExp

#class labels
classes = ['','CO-USE_COMBUST_MJ_COMBUST_TOBACCO', 'DUAL-USE_COMBUST_MJ_VAPING_MJ', 'DUAL-USE_COMBUST_MJ_VAPE_NIC/TOBACCO', 'DUAL-USE_COMBUST_MJ_COMBUST_TOBACCO', 'DUAL-USE_VAPING_MJ_VAPING_NIC/TOBACCO','DUAL-USE_COMBUST_TOBACCO_VAPING_NIC/TOBACCO','DUAL-USE_VAPING_MJ_COMBUST_TOBACCO','POLY-USE_COMBUST_TOBACCO_COMBUST_MJ_VAPING_MJ','POLY-USE_COMBUST_TOBACCO_COMBUST_MJ_VAPING_NIC/TOBACCO','POLY_USE_COMBUST_TOABBCO_VAPING_MJ_VAPING_NIC/TOBACCO','POLY_USE_COMBUST_MJ_VAPING_MJ_VAPING_NIC/TOBACCO','COMBUST_MJ','COMBUST_TOBACCO','VAPING_MJ','VAPING_NIC/TOBACCO','BRAND','VAPING','SMOKING_CESSATION']

#load feature data with filename
data1 = pickle.load( open( "4_10_findAnotData.p", "rb" ) )
data2 = pickle.load( open( "11_50_findAnotData.p", "rb" ) )
data3 = pickle.load( open( "51_100_findAnotData.p", "rb" ) )
data4 = pickle.load( open( "101_218_findAnotData.p", "rb" ) )
data5 = pickle.load( open( "218_1000_findAnotData.p", "rb" ) )

featData = data1 + data2+data3+data4+data5


totalCorrect = 0
totalAnnot = 0
totalRulebased = 0

y_pred = []
y_true = []
for d in featData:
	corpusFilename = d['filename']
	parseList = corpusFilename.split('/')
	adjudicationFilename = '/'.join(parseList[0:-2])+'/Adjudication/'+parseList[-1]+'.knowtator.xml'
	subreddit = parseList[-1].split('_')[-1].replace('.txt','')

	#get corpus data and annotation data
	anotDicList = reader.annotFileReader(adjudicationFilename)
	corpusData = reader.corpusFileReader(corpusFilename)

	#rule based
	#ruleBasedAnnotList = RegExp.regExDetect(corpusData)
	ruleBasedAnnotList = RegExp.regExDetect_subreddit(corpusData, subreddit)

	correctNum=0
	for r in ruleBasedAnnotList:
		rStart = r['start']
		rEnd = r['end']
		rCat = r['category']
		#y_pred.append(rCat)
		isFind = 0
		for a in anotDicList:
			aStart = a['start']
			aEnd = a['end']
			aCat = a['class']
			if min(aEnd,rEnd)-max(aStart,rStart)>0 and aCat==rCat:
				correctNum = correctNum+1
				y_true.append(aCat)
				y_pred.append(aCat)
				isFind = 1
			elif min(aEnd,rEnd)-max(aStart,rStart)>0 and not(aCat==rCat):
				y_pred.append(rCat)
				y_true.append(aCat)
				isFind = 1
		if isFind==0:
			y_true.append('')
			y_pred.append(rCat)

	#print('current Precision:',  correctNum/float(len(ruleBasedAnnotList)),'current recall', correctNum/float(len(anotDicList)))

	totalCorrect = totalCorrect +correctNum
	totalAnnot = totalAnnot + len(anotDicList)
	totalRulebased = totalRulebased + len(ruleBasedAnnotList)	

print('total correct:', totalCorrect)
print('total annotation:', totalAnnot)
print('rule based annot:',totalRulebased)
print('Overall Precision:', totalCorrect/float(totalRulebased),'total recall:',totalCorrect/float(totalAnnot) )			

from sklearn.metrics import confusion_matrix
import performanceMetric
confusionMatrix = confusion_matrix(y_true, y_pred, labels=classes)

for i in range(len(classes)):
	specificity = performanceMetric.specificity(i,confusionMatrix)
	precision = performanceMetric.precision(i,confusionMatrix)
	recall = performanceMetric.recall(i,confusionMatrix)

	print(classes[i],'specificity:',specificity,'precision:',precision,'recall:',recall)

overallPrecision = performanceMetric.precision_macro_average(confusionMatrix)
overallRecall = performanceMetric.recall_macro_average(confusionMatrix)
overallAccuracy = performanceMetric.accuracy(confusionMatrix)
overallSpecificity = performanceMetric.specificity_macro_average(confusionMatrix)
print('overallSpecificity:',overallSpecificity, 'overallPrecision:',overallPrecision,'overallRecall:',overallRecall,'overallaccuracy:',overallAccuracy)
