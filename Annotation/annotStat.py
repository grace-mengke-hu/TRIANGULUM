#!../../anaconda2/bin/python

import re
import pickle
import reader
import RegExp
import spacy
import CRFfeature

from itertools import chain
import nltk
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelBinarizer
import sklearn
import pycrfsuite
import time

#load spacy english model
nlp = spacy.load("en_core_web_sm")


#load feature data with filename
data1 = pickle.load( open( "4_10_findAnotData.p", "rb" ) )
data2 = pickle.load( open( "11_50_findAnotData.p", "rb" ) )
data3 = pickle.load( open( "51_100_findAnotData.p", "rb" ) )
data4 = pickle.load( open( "101_218_findAnotData.p", "rb" ) )
data5 = pickle.load( open( "218_1000_findAnotData.p", "rb" ) )

featData = data1+data2+data3+data4+data5

numFpoly = 0
numFdual = 0
numFstop = 0
numFco = 0
numF = 0
numV = 0
poly = []
dual = []
stop = []
co = []
v = []
for d in featData: #[featData[0]]:#test on one sample
	corpusFilename = d['filename']
	parseList = corpusFilename.split('/')
	adjudicationFilename = '/'.join(parseList[0:-2])+'/Adjudication/'+parseList[-1]+'.knowtator.xml'
	subreddit = parseList[-1].split('_')[-1].replace('.txt','')
	user = parseList[-1].split('_')[1]
	#get corpus data and annotation data
	anotDicList = reader.annotFileReader(adjudicationFilename)
	corpusData = reader.corpusFileReader(corpusFilename)
	numF = numF+1

	pInd = 0
	dInd = 0
	sInd = 0
	coInd = 0
	vInd = 0
	for anot in anotDicList:
		if 'POLY' in anot['class']:
			pInd = 1			
		if 'DUAL' in anot['class']:
			dInd = 1		
		if 'CESSATION' in anot['class']:
			sInd = 1			
		if 'CO-USE' in anot['class']:
			coInd = 1
		if 'VAPING_MJ' in anot['class']:
			vInd = 1

	if pInd ==1:
		numFpoly = numFpoly+1
		poly.append(user)
	if dInd ==1:
		numFdual = numFdual+1
		dual.append(user)
	if sInd ==1:
		numFstop = numFstop+1
		stop.append(user)
	if coInd ==1:
		numFco = numFco+1
		co.append(user)
	if vInd ==1:
		numV = numV+1
		v.append(user)
print('--------poly---------')
print(set(poly))
print('--------dual---------')
print(set(dual))
print('--------stop---------')
print(set(stop))
print('--------co---------')
print(set(co))
print('--------V----------')
print(set(v))


print('total:',numF,'poly:',numFpoly,'dual:',numFdual,'stop:',numFstop,'co:',numFco,'v:',numV)

