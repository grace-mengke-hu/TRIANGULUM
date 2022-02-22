#!../../anaconda2/bin/python
import os
import reader
import label
import numpy as np



classLabelDic = label.classLabel()
relationLabelList = label.relationLabel()

dir1 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/4-10/"
dir2 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/11-50/"
dir3 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/51-100/"
dir4 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/101-218/"
dir5 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/218-1000/"

#path for each corpus file
dirList = [dir1,dir2,dir3,dir4,dir5]
pathList = []
for d in dirList:
	for f in os.listdir(d+'Corpus'):
		pathList.append(d+'Corpus/'+f)

#get user dictionary time sort
userPathDic = {}
for dirPath in pathList:
	fname = dirPath.split('/')[-1]
	#print(fname)
	if "electronic_cigarette" in fname:
		parseList = fname.split('_')
		#unixTime = parseList[-4]
		#userName = parseList[-5]
		if parseList[-5] in userPathDic.keys():
			userPathDic[parseList[-5]].append({'time':int(parseList[-4]),'path':dirPath})
			#userPathDic[parseList[-5]].append({parseList[-4]:dirPath})
		else:
			userPathDic[parseList[-5]] = []
	else:
		parseList = fname.split('_')
		#unixTime = parseList[-3]
		#userName = parseList[-4]
		if parseList[-4] in userPathDic.keys():
			userPathDic[parseList[-4]].append({'time':int(parseList[-3]),'path':dirPath})
			#userPathDic[parseList[-4]].append({parseList[-3]:dirPath})
		else:
			userPathDic[parseList[-4]] = []

print(list(userPathDic.items())[2])
print(userPathDic.keys())

for user in userPathDic.keys():
	for timeCorpusDic in userPathDic[user]: #list of dic
#		for  k in timeCorpusDic.keys():
		currentCorpusFilePath = timeCorpusDic['path']
		currentAnnotFilePath = timeCorpusDic['path'].replace('Corpus','Adjudication')+'.knowtator.xml'
		#subreddit
		subreddit = ''
		if "electronic_cigarette" in currentCorpusFilePath:
			subreddit = "electronic_cigarette"
		else:				subreddit = currentCorpusFilePath.split('_')[-1].replace('.txt','').lower()
		timeCorpusDic['subreddit'] = subreddit

		#labelGen
		#read in file sequence
		annotDicList = reader.annotFileReader_relationship(currentAnnotFilePath)
		corpusData = reader.corpusFileReader(currentCorpusFilePath)
		timeCorpusDic['corpus'] = corpusData

		#get label and relations for annot data
		classLabelSet = set()
		relationLabelSet = set()
		if annotDicList:
			for annot in annotDicList:
				classLabelSet.add(annot['class'])
				if annot['relationList']:
					for r in annot['relationList']:
						relationLabelSet.add(r['relation'])
				else:
					relationLabelSet.add(' ')
		else:
			classLabelSet.add(' ')

		#generate label for current post classLabelDic
		postAnnot = []
		for l in list(classLabelSet):
			postAnnot = postAnnot+classLabelDic[l]
		genClassLabel = label.labelGen(list(set(postAnnot)))
		genRelLabel = label.relLabelGen(list(relationLabelSet))
		genLabel = genClassLabel+genRelLabel
		timeCorpusDic['genLabel'] = genLabel

print(list(userPathDic.items())[2])		

import pickle
pickle.dump(userPathDic, open('postLevelPerUserDic.p','wb'))
