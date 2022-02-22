#!../../anaconda2/bin/python
import os
import reader
import label
import numpy as np
from gensim.models.doc2vec import Doc2Vec
from gensim.models import Word2Vec
import spacy

#load spacy english model
nlp = spacy.load("en_core_web_sm")

#load doc2vec
doc2vecModel = Doc2Vec.load('/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/enwiki_dbow/doc2vec.bin')

#load word2vec
word2vecModel = Word2Vec.load("/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/word2vec.bin")


classLabelDic = label.classLabel()
relationLabelList = label.relationLabel()

dir1 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/4-10/"
dir2 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/11-50/"
dir3 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/51-100/"
dir4 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/101-218/"
dir5 = "/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/218-1000/"

dirList = [dir1,dir2,dir3,dir4,dir5]
pathList = []
for d in dirList:
	for f in os.listdir(d+'Corpus'):
		pathList.append(d+'Corpus/'+f)


timePathDic = {}


for dirPath in pathList:
	fname = dirPath.split('/')[-1]
	print(fname)
	if "electronic_cigarette" in fname:
		parseList = fname.split('_')
		#unixTime = parseList[-4]
		userName = parseList[-5]
		timePathDic[parseList[-4]] = dirPath #+ fname
	else:
		parseList = fname.split('_')
		#unixTime = parseList[-3]
		userName = parseList[-4]
		timePathDic[parseList[-3]] = dirPath #+ fname

corpusList = []
featureList = []
labelList = []		
timeList = timePathDic.keys()
timeList.sort()
for t in timeList:
	currentCorpusFilePath = timePathDic[t]
	currentAnnotFilePath = timePathDic[t].replace('Corpus','Adjudication')+'.knowtator.xml'
	subreddit = ''
	if "electronic_cigarette" in currentCorpusFilePath:
		subreddit = "electronic_cigarette"
	else:
		subreddit = currentCorpusFilePath.split('_')[-1].replace('.txt','').lower()

	#read in file sequence
	annotDicList = reader.annotFileReader_relationship(currentAnnotFilePath)
        corpusData = reader.corpusFileReader(currentCorpusFilePath)

	#get label and relations for annot data
	classLabelSet = set()
	relationLabelSet = set()
	if annotDicList:
		#classLabelSet = set()
		for annot in annotDicList:
			classLabelSet.add(annot['class'])
			if annot['relationList']:
				#relationLabelSet = set()
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
	labelList.append(genLabel)

	#doc2vec vector
	corpusDoc = nlp(corpusData.decode('UTF8'))
	corpusWordList = []
	for w in corpusDoc:
		corpusWordList.append(w.text)
	docVector = doc2vecModel.infer_vector(corpusWordList)
	featureList.append(docVector)
	corpusList.append(corpusData)

import pickle
pickle.dump(corpusList,open('postLevelCorpustList.p','wb'))
pickle.dump(featureList,open('postLevelFeatureList.p','wb'))
pickle.dump(labelList,open('postLebelLabelList.p','wb'))
