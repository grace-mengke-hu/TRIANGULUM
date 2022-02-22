#!../../anaconda2/bin/python


import os
#import shutil
#import random
#import re
#import json
#import pickle
import reader

#dir1 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/4-10/"#Adjudication/"
#dir2 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/11-50/"#Adjudication/"
#dir3 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/51-100/"
#dir4 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/101-218/"
#dir5 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/218-1000/"
dir3 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-07-05/"#Adjudication/"
dir4 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-07-15/"#Adjudication/"
dir5 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-07-22/"#Adjudication/"
dir6 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-07-29/"#Adjudication/"
dir7 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-08-05/"#Adjudication/"
dir8 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-08-20/"#Adjudication/"
dir9 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/2019-09-04/"#Adjudication/"

dirPath = dir9
fileSet = set()
for filename in os.listdir(dirPath+"Adjudication/"):
	anotDicList = reader.annotFileReader_relationship(dirPath+"Adjudication/"+filename)
	for t in anotDicList:
		if t['relationList']:
			fileSet.add(filename)

#.knowtator.xml
for fp in list(fileSet):
	os.system('cp '+dirPath+"Adjudication/"+fp+' '+'/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/RelationshipData/Adjudication/')
	os.system('cp '+dirPath+"rawData/"+fp.replace('.knowtator.xml','')+' '+'/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/RelationshipData/Corpus/')
	os.system('mv '+'/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/RelationshipData/Adjudication/'+fp+ ' '+'/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/RelationshipData/Adjudication/'+'annotSchema_'+fp[4:])
	os.system('mv '+'/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/RelationshipData/Corpus/'+fp.replace('.knowtator.xml','') + ' '+'/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/RelationshipData/Corpus/'+'annotSchema_'+fp.replace('.knowtator.xml','')[4:])
