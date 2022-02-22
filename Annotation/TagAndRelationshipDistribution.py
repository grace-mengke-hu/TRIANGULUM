#!../../anaconda2/bin/python


import os
#import shutil
#import random
#import re
#import json
#import pickle
import reader

dir1 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/4-10/Adjudication/"
dir2 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/11-50/Adjudication/"
dir12 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/51-100/Adjudication/"
dir13 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/101-218/Adjudication/"
dir14 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/218-1000/Adjudication/"
dir3 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-07-05/Adjudication/"
dir4 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-07-15/Adjudication/"
dir5 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-07-22/Adjudication/"
dir6 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-07-29/Adjudication/"
dir7 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-08-05/Adjudication/"
dir8 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-08-20/Adjudication/"
dir9 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-09-04/Adjudication/"
dir10 = '/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/RelationshipData/Adjudication/'

allAnotList = []
numFiles = 0
numRelationship = 0
numAnotFile = 0
numNoneFile = 0
numNoneRelFile = 0
numNoneRelFile = 0
for filename in os.listdir(dir1):
	anotDicList = reader.annotFileReader_relationship(dir1+filename)
	if anotDicList:
		numAnotFile = numAnotFile+1
	else:
		numNoneFile = numNoneFile+1
	
	allAnotList = allAnotList+anotDicList
	currentRel = 0
	for t in anotDicList:
		if t['relationList']:
#			print(filename)
			numRelationship = numRelationship + len(t['relationList'])
			currentRel = currentRel + len(t['relationList'])
			print(t['relationList'])
	if currentRel ==0:
		numNoneRelFile = numNoneRelFile+1
	else:
		numFiles = numFiles+1

print('numAnot:',numAnotFile,'num none:',numNoneFile)
print('num relate files:', numFiles,'num none relate:',numNoneRelFile)
#print('total relation files:',len(os.listdir(dir1)))
print('total relationships:',numRelationship)
print('total annotation:',len(allAnotList))


