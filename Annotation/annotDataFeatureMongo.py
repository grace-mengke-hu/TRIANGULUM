#!../../anaconda2/bin/python


import os
import shutil
import random
import re
#import json
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client['Reddit_R21']
collectionList = db.collection_names()
print(collectionList)

#annotation data location
files1 = os.listdir('/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/RelationshipData/Corpus/')
#('/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/218-1000/Corpus/')
#('/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/eHostWorkSpace/4_10_batch9/corpus/')
#files3 = os.listdir('/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/eHostWorkSpace/4_10_batch3/corpus/')
#files4 = os.listdir('/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/eHostWorkSpace/4_10_batch4/corpus/')
#files5 = os.listdir('/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/eHostWorkSpace/4_10_batch5/corpus/')
annotFiles = files1#+files3+files4+files5


print(annotFiles)

listData = []
subredditDic = {'Marijuana':'marijuana','Vaping':'vaping','Cigarette':'Cigarettes','cigarettes':'Cigarettes'}
for docFile in annotFiles:
	#read in text file from corpus
	with open('/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/RelationshipData/Corpus/'+docFile) as fp:
   		lines = fp.readlines()
	docText = ' '.join(lines)

	#find mongoDB
	if 'electronic_cigarette' in docFile:
		parseList = docFile.split('_')
		subredditName = 'electronic_cigarette'
		postID = parseList[-3]
		utc = parseList[-4]
		userName = '_'.join(parseList[1:-4])
	else:
		parseList = docFile.split('_')
		subredditName = parseList[-1][0:-4]
	#print(subredditName)
		postID = parseList[-2]
		utc = parseList[-3]
		userName = '_'.join(parseList[1:-3])
	
	if subredditName in collectionList:
		collection = db[subredditName]
		print(docFile)
		findData = collection.find_one({"id":postID})
		findData['filename'] = '/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/RelationshipData/Corpus/'+docFile
		listData.append(findData)		
		#print(docText)
		#print("----------------")
		#print(findData['title'])
	else:
		print(docFile)
		collection = db[subredditDic[subredditName]]
		#print(docFile)
		findData= collection.find_one({"id":postID})
		findData['filename'] = '/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/RelationshipData/Corpus/'+docFile
		listData.append(findData)		
		print(subredditName)
	#print(subredditName)
	#collection = db[subredditName]	

import pickle
pickle.dump(listData, open( "relationships_findAnotData.p", "wb" ) )
		
			
			

