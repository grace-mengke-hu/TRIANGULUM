#!../../anaconda2/bin/python


#import os
#import shutil
#import random
import re
#import json
import pickle
import reader
import RegExp

#load feature data with filename
data1 = pickle.load( open( "4_10_findAnotData.p", "rb" ) )
data2 = pickle.load( open( "11_50_findAnotData.p", "rb" ) )
data3 = pickle.load( open( "51_100_findAnotData.p", "rb" ) )
data4 = pickle.load( open( "101_218_findAnotData.p", "rb" ) )
data5 = pickle.load( open( "218_1000_findAnotData.p", "rb" ) )

featData = data1 + data2+data3+data4+data5

concepts = ['VAPING_MJ','VAPING_NIC/TOBACCO','COMBUST_MJ','COMBUST_TOBACCO','BRAND','SMOKING_CESSATION']

totalCorrect = 0
totalAnnot = 0
totalRulebased = 0
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
	#	print(subreddit)
#print('-----------')
#for t in ruleBasedAnnotList:
#	print(t)
#print(ruleBasedAnnotList)

	correctNum=0
	for r in ruleBasedAnnotList:
		rStart = r['start']
		rEnd = r['end']
		rCat = r['category']
		if rCat in concepts:
			for a in anotDicList:
				aStart = a['start']
				aEnd = a['end']
				aCat = a['class']
				if min(aEnd,rEnd)-max(aStart,rStart)>0 and aCat==rCat:
					correctNum = correctNum+1
	#print('current Precision:',  correctNum/float(len(ruleBasedAnnotList)),'current recall', correctNum/float(len(anotDicList)))

	totalCorrect = totalCorrect +correctNum
	totalAnnot = totalAnnot + len(anotDicList)
	totalRulebased = totalRulebased + len(ruleBasedAnnotList)	

print('total correct:', totalCorrect)
print('total annotation:', totalAnnot)
print('rule based annot:',totalRulebased)
print('Overall Precision:', totalCorrect/float(totalRulebased),'total recall:',totalCorrect/float(totalAnnot) )			
