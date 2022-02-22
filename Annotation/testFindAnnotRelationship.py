#!../../anaconda2/bin/python


import os
import shutil
import random
import re
import json
import pickle

##load feature data with filename
#featData = pickle.load( open( "4_10_batch1_findAnotData.p", "rb" ) )

##take only one filename to test
#corpusFilename = featData[0]['filename']

filename = '9_possumknowsbest_1435175862_3azmmx_trees.txt.knowtator.xml'
#get adjudication filename: /uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/eHostWorkSpace/4_10_batch1/corpus/9_jd_246_1523844165_8ck5iq_trees.txt
#parseList = corpusFilename.split('/')
#adjudicationFilename = '/'.join(parseList[0:-2])+'/adjudication/'+parseList[-1]+'.knowtator.xml'


import reader
anotDicList = reader.annotFileReader_relationship(filename)
for t in anotDicList:
	print(t)


