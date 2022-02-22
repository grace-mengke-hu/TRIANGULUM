#!../../anaconda2/bin/python
import pickle
import label

labelDic = label.simpleConceptLabel()#label.classLabel()


#tobacco
timeList_t = pickle.load(open("vaping_submissionUTC_2013-2018.p","rb"))
LSTMpred_t = pickle.load(open("vaping_submissionLSTMpredict_2013-2018.p","rb"))

#print(LSTMpred_t[0])
timeLabelDic = {}
for i in range(len(LSTMpred_t)):
	postLabel = []
	for sent in LSTMpred_t[i]:
		for token in sent:
			if token in labelDic.keys():
				postLabel = postLabel+labelDic[token]
			
					
	timeLabelDic[timeList_t[i]] = list(set(postLabel))


pickle.dump(timeLabelDic, open('vaping_timeLSTMcatDicSimple_2013-2018.p','wb'))

#print(len(timeList_t),len(LSTMpred_t))

















