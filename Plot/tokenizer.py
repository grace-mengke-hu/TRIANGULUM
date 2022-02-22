#!../../anaconda2/bin/python

import pickle
import spacy

#load spacy english model
nlp = spacy.load("en_core_web_sm")

posts = pickle.load( open( "cessation_submissionTXT_2013-2018.p", "rb" ) )
postsSentsLabel = []
for p in posts:
	P_sentsTokenDic = {}
	doc = nlp(p.encode('utf-8').decode('utf-8','ignore'))
	for x in doc:
		if str(x.sent) in P_sentsTokenDic.keys():
			P_sentsTokenDic[str(x.sent)].append(str(x))
		else:
			P_sentsTokenDic[str(x.sent)] = []
			P_sentsTokenDic[str(x.sent)].append(str(x))

		#list of sentences(list of tokens) for current post
	currentSentence = P_sentsTokenDic.values()
	postsSentsLabel.append(P_sentsTokenDic)


#list of dictionary
print(postsSentsLabel[0:2])
pickle.dump(postsSentsLabel, open('cessation_submissionSentToken_2013-2018.p','wb'))

