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
corpusFilename = featData[0]['filename']

#get adjudication filename: /uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/eHostWorkSpace/4_10_batch1/corpus/9_jd_246_1523844165_8ck5iq_trees.txt
parseList = corpusFilename.split('/')
adjudicationFilename = '/'.join(parseList[0:-2])+'/adjudication/'+parseList[-1]+'.knowtator.xml'


import reader
anotDicList = reader.annotFileReader(adjudicationFilename)
for t in anotDicList:
	print(t)
corpusData = reader.corpusFileReader(corpusFilename)
print(corpusData[576:580])
print(len(corpusData.split('\n\n')))

print(corpusData.split('\n\n')[0])
print('-----------')
print(featData[0]['title'])
if corpusData.split('\n\n')[0] == featData[0]['title']:
	print('yes')
