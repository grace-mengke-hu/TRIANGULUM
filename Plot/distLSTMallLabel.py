#!../../anaconda2/bin/python

import pickle
import label

postsLabel = pickle.load(open("MJ_submissionLSTMpredict_2013-2018.p","rb"))

labelDic = label.classLabel()
labels = labelDic.keys()
print(labels)
#print(postsLabel[0]) #list of tokenized sentences
allPostLabels = []
for p in postsLabel:
	postLabels = set()
	for sent in p:
		for l in sent:
			if l in labels:
				postLabels.add(l)
	allPostLabels.append(list(postLabels))	

noLabelPost = 0
labeledPost = 0
for a in allPostLabels:
	if not (a):
		noLabelPost =noLabelPost +1
	else:
		labeledPost = labeledPost+1
print('no labeled:',noLabelPost,'labeled post:',labeledPost)

for l in labels:
	numPost = 0
	for p in allPostLabels:
		if l.decode('utf-8') in p:
			numPost = numPost+1
	print('label:',l, 'post frequency:',numPost) 	





