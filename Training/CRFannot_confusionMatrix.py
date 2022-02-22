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

sentsTokenDic = {}
for d in featData: #[featData[0]]:#test on one sample
	corpusFilename = d['filename']
	parseList = corpusFilename.split('/')
	adjudicationFilename = '/'.join(parseList[0:-2])+'/Adjudication/'+parseList[-1]+'.knowtator.xml'
	subreddit = parseList[-1].split('_')[-1].replace('.txt','')
	#get corpus data and annotation data
	anotDicList = reader.annotFileReader(adjudicationFilename)
	corpusData = reader.corpusFileReader(corpusFilename)

	#NLP NER and Annotation
	doc = nlp(corpusData.decode('UTF8'))
	#sentsTokenDic = {}
	#dataSentList = []
	for x in doc:
	
		#search for the annotation for this token
		xStart = x.idx
		xEnd = x.idx+len(x.text)-1
		classLabel = ''
		for anot in anotDicList:
			if min(anot['end'],xEnd)-max(anot['start'],xStart) >0:
				classLabel = anot['class']

		if str(x.sent) in sentsTokenDic.keys():#REMARK: here str() is to convert any UTF8 char in string
			sentsTokenDic[str(x.sent)].append((str(x).decode('utf-8', 'ignore'), x.ent_type_, classLabel.decode('utf-8') ))
		else:#new sentence
			sentsTokenDic[str(x.sent)] = []
		

#print(sentsTokenDic)	
print('number of sentences: ',len(sentsTokenDic))

#Form training and testing data
sentenceData = sentsTokenDic.values()
#print(sentenceData[0])
X_train = [CRFfeature.sent2features(s) for s in sentenceData[0:2500]]
y_train = [CRFfeature.sent2labels(s) for s in sentenceData[0:2500]]

X_test = [CRFfeature.sent2features(s) for s in sentenceData[2500:]]
y_test = [CRFfeature.sent2labels(s) for s in sentenceData[2500:]]

#create pycrfsuite.Trainer and load the training data to CRFsuite
time_start = time.time()
trainer = pycrfsuite.Trainer(verbose=False)

for xseq, yseq in zip(X_train, y_train):
	trainer.append(xseq, yseq)

#Set training parameters. We will use L-BFGS training algorithm (it is default) with Elastic Net (L1 + L2) regularization.
trainer.set_params({
    'c1': 1.0,   # coefficient for L1 penalty
    'c2': 1e-3,  # coefficient for L2 penalty
    'max_iterations': 50,  # stop earlier

    # include transitions that are possible, but not observed
    'feature.possible_transitions': True
})
print(trainer.params())
time_train_end = time.time()
print("TRAINING TIME:", time_train_end-time_start)

#Training
#%%time
trainer.train('redditUserBasedBin.crfsuite')
print(trainer.logparser.last_iteration)

##Testing
tagger = pycrfsuite.Tagger()
tagger.open('redditUserBasedBin.crfsuite')
y_pred = [tagger.tag(xseq) for xseq in X_test]
time_test_end = time.time()
print("TESTING TAGGING:",time_test_end-time_start)

#print(y_test,y_pred)

#merge to one list
yTrue = []
yPred = []
for i in range(len(y_test)):
	yTrue = yTrue+y_test[i]
	yPred = yPred+y_pred[i]
#evaluation
#class labels
classes = ['','CO-USE_COMBUST_MJ_COMBUST_TOBACCO', 'DUAL-USE_COMBUST_MJ_VAPING_MJ', 'DUAL-USE_COMBUST_MJ_VAPE_NIC/TOBACCO', 'DUAL-USE_COMBUST_MJ_COMBUST_TOBACCO', 'DUAL-USE_VAPING_MJ_VAPING_NIC/TOBACCO','DUAL-USE_COMBUST_TOBACCO_VAPING_NIC/TOBACCO','DUAL-USE_VAPING_MJ_COMBUST_TOBACCO','POLY-USE_COMBUST_TOBACCO_COMBUST_MJ_VAPING_MJ','POLY-USE_COMBUST_TOBACCO_COMBUST_MJ_VAPING_NIC/TOBACCO','POLY_USE_COMBUST_TOABBCO_VAPING_MJ_VAPING_NIC/TOBACCO','POLY_USE_COMBUST_MJ_VAPING_MJ_VAPING_NIC/TOBACCO','COMBUST_MJ','COMBUST_TOBACCO','VAPING_MJ','VAPING_NIC/TOBACCO','BRAND','VAPING','SMOKING_CESSATION']

from sklearn.metrics import confusion_matrix
import performanceMetric
confusionMatrix = confusion_matrix(yTrue, yPred, labels=classes)

for i in range(len(classes)):
        specificity = performanceMetric.specificity(i,confusionMatrix)
        precision = performanceMetric.precision(i,confusionMatrix)
        recall = performanceMetric.recall(i,confusionMatrix)

        print(classes[i],'specificity:',specificity,'precision:',precision,'recall:',recall)

overallPrecision = performanceMetric.precision_macro_average(confusionMatrix)
overallRecall = performanceMetric.recall_macro_average(confusionMatrix)
overallAccuracy = performanceMetric.accuracy(confusionMatrix)
overallSpecificity = performanceMetric.specificity_macro_average(confusionMatrix)
print('overallSpecificity:',overallSpecificity, 'overallPrecision:',overallPrecision,'overallRecall:',overallRecall,'overallaccuracy:',overallAccuracy)

