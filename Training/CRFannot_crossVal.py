#!../../anaconda2/bin/python

import re
import pickle
import reader
import RegExp
import spacy
import CRFfeature

from itertools import chain

import nltk
import sklearn
import scipy.stats
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score
#from sklearn.cross_validation import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
#from sklearn.grid_search import RandomizedSearchCV

import sklearn_crfsuite
from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics
import numpy as np
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
X_train = [CRFfeature.sent2features(s) for s in sentenceData[0:2500]]
y_train = [CRFfeature.sent2labels(s) for s in sentenceData[0:2500]]
X_test = [CRFfeature.sent2features(s) for s in sentenceData[2500:]]
y_test = [CRFfeature.sent2labels(s) for s in sentenceData[2500:]]

#get the label from training data
crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=100,
    all_possible_transitions=True
)
crf.fit(X_train, y_train)

#Evaluation ['COMBUST_MJ', 'VAPING_NIC/TOBACCO', 'SMOKING_CESSATION', 'COMBUST_TOBACCO', 'BRAND', 'CO-USE_COMBUST_MJ_COMBUST_TOBACCO', 'VAPING_MJ', 'VAPING']
labels = ['CO-USE_COMBUST_MJ_COMBUST_TOBACCO', 'DUAL-USE_COMBUST_MJ_VAPING_MJ', 'DUAL-USE_COMBUST_MJ_VAPE_NIC/TOBACCO', 'DUAL-USE_COMBUST_MJ_COMBUST_TOBACCO', 'DUAL-USE_VAPING_MJ_VAPING_NIC/TOBACCO','DUAL-USE_COMBUST_TOBACCO_VAPING_NIC/TOBACCO','DUAL-USE_VAPING_MJ_COMBUST_TOBACCO','POLY-USE_COMBUST_TOBACCO_COMBUST_MJ_VAPING_MJ','POLY-USE_COMBUST_TOBACCO_COMBUST_MJ_VAPING_NIC/TOBACCO','POLY_USE_COMBUST_TOABBCO_VAPING_MJ_VAPING_NIC/TOBACCO','POLY_USE_COMBUST_MJ_VAPING_MJ_VAPING_NIC/TOBACCO','COMBUST_MJ','COMBUST_TOBACCO','VAPING_MJ','VAPING_NIC/TOBACCO','BRAND','VAPING','SMOKING_CESSATION']
#labels = list(crf.classes_)
#labels.remove('')
#print("LABELS: ",labels)
y_pred = crf.predict(X_test)
print(metrics.flat_f1_score(y_test, y_pred, average='weighted', labels=labels))

sorted_labels = sorted(labels)
#    key=lambda name: (name[1:], name[0])
#)
print(metrics.flat_classification_report(y_test, y_pred, labels=sorted_labels, digits=3))


#Hyperparameter optimization
# define fixed parameters and parameters to search
crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    max_iterations=100,
    all_possible_transitions=True
)

params_space = {
    'c1': scipy.stats.expon(scale=0.5),
    'c2': scipy.stats.expon(scale=0.05),
}

# use the same metric for evaluation
f1_scorer = make_scorer(metrics.flat_f1_score, average='weighted', labels=labels)

# search
rs = RandomizedSearchCV(crf, params_space,
                        cv=3,
                        verbose=1,
                        n_jobs=-1,
                        n_iter=50,
                        scoring=f1_scorer)

rs.fit(X_train+X_test, y_train+y_test)

print('best params:', rs.best_params_)
print('best CV score:', rs.best_score_)
print('model size: {:0.2f}M'.format(rs.best_estimator_.size_ / 1000000))


