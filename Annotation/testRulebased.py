#!../../anaconda2/bin/python


import os
import shutil
import random
import re
import json
import pickle

#load feature data with filename
featData = pickle.load( open( "4_10_batch1_findAnotData.p", "rb" ) )

#take only one filename to test
corpusFilename = featData[1]['filename']

#get adjudication filename: /uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/eHostWorkSpace/4_10_batch1/corpus/9_jd_246_1523844165_8ck5iq_trees.txt
parseList = corpusFilename.split('/')
adjudicationFilename = '/'.join(parseList[0:-2])+'/adjudication/'+parseList[-1]+'.knowtator.xml'
subreddit = parseList[-1].split('_')[-1].replace('.txt','')

#read annotation and corpus data
import reader
anotDicList = reader.annotFileReader(adjudicationFilename)
for t in anotDicList:
	print(t)
corpusData = reader.corpusFileReader(corpusFilename)
#print(corpusData)

#Rule based
import RegExp 
#import re

ruleBasedAnnotList = RegExp.regExDetect_subreddit(corpusData, subreddit)
print(subreddit)
#print(anotDicList)
print('-----------')
for t in ruleBasedAnnotList:
	print(t)
#print(ruleBasedAnnotList)

correctNum=0
for r in ruleBasedAnnotList:
	rStart = r['start']
	rEnd = r['end']
	rCat = r['category']
	for a in anotDicList:
		aStart = a['start']
		aEnd = a['end']
		aCat = a['class']
		if min(aEnd,rEnd)-max(aStart,rStart)>0 and aCat==rCat:
			correctNum = correctNum+1

print('Average Precision:', correctNum, correctNum/float(len(ruleBasedAnnotList)))			
