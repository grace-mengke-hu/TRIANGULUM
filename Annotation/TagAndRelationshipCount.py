#!../../anaconda2/bin/python


import os
#import shutil
#import random
#import re
#import json
#import pickle
import reader
import label

dir1 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/4-10/Adjudication/"
dir2 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/11-50/Adjudication/"
dir3 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/51-100/Adjudication/"
dir4 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/101-218/Adjudication/"
dir5 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/218-1000/Adjudication/"

dirList = [dir1,dir2,dir3,dir4,dir5]

allAnotList = []
numFiles = 0
numRelationship = 0
numAnotFile = 0
numNoneFile = 0
numNoneRelFile = 0
numNoneRelFile = 0

classLabelDic = label.classLabel()
relList = []
MJ = 0
TOBACCO = 0
VAPING = 0
CESSATION = 0
fileClassLabelList = []
for d in dirList:
	for filename in os.listdir(d):
		anotDicList = reader.annotFileReader_relationship(d+filename)
		anotSet = set()
		if anotDicList:
			for t in anotDicList:
				if t['relationList']:
					for r in t['relationList']:
						relList.append(r['relation'])

				anotSet.add(t['class'])					
		postAnnot = []
		for l in list(anotSet):
			postAnnot = postAnnot+classLabelDic[l]

		fileClassLabelList.append(list(set(postAnnot)))


import collections
counter = collections.Counter(relList)
print(counter)

for f in fileClassLabelList:
	if 'MJ' in f:
		MJ = MJ+1
	if 'VAPING' in f:
		VAPING = VAPING+1
	if 'CESSATION' in f:
		CESSATION = CESSATION+1
	if 'TOBACCO' in f:
		TOBACCO = TOBACCO+1

print('MJ',MJ, 'VAPING', VAPING, 'CESSATION', CESSATION, 'TOBACCO',TOBACCO)
