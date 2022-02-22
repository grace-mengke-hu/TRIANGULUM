#!../../anaconda2/bin/python


import os
import shutil
import random
import re
import json
import pickle
import reader

#load feature data with filename
featData = pickle.load( open( "218_1000_findAnotData.p", "rb" ) )

numAnnot = 0
for fileData in featData:
	fname = fileData['filename']
	parseList = fname.split('/')
	adjudicationFilename = '/'.join(parseList[0:-2])+'/Adjudication/'+parseList[-1]+'.knowtator.xml'
	anotDicList = reader.annotFileReader(adjudicationFilename)
	for t in anotDicList:
		numAnnot = numAnnot+1

print(numAnnot)

