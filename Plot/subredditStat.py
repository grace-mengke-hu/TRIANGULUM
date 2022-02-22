#!../../anaconda2/bin/python

import json
from collections import Counter
import pickle

#Tobacco
with open("../../Data/cig2013-2018.json","r") as read_file:
	data = json.load(read_file)

##Vaping
#with open("../../Data/e_cig2013-2018.json","r") as read_file:
#	dataEcig = json.load(read_file)
#with open("../../Data/vaping2013-2018.json","r") as read_file:
#	dataVaping = json.load(read_file)
#with open("../../Data/Vaping101_2013-2018.json","r") as read_file:
#	dataVaping101 = json.load(read_file)
#dataVaping = dataEcig+dataVaping+dataVaping101

##Marijuana
#with open("../../Data/marijuana2013-2018.json","r") as read_file:
#	dataMarijuana = json.load(read_file)
#with open("../../Data/marijuanaEnthusiast2013-2018.json","r") as read_file:
#        dataMen = json.load(read_file)
#with open("../../Data/trees_2013-2018.json","r") as read_file:
#        dataTree = json.load(read_file)
#with open("../../Data/weed2013-2018.json","r") as read_file:
#        dataWeed = json.load(read_file)
#dataMJ = dataMarijuana+dataMen+dataTree+dataWeed

##stop smoking
#with open("../../Data/stopsmoking2013-2018.json","r") as read_file:
#        dataCessation = json.load(read_file)


#number of posts
authorList = []
numpost = 0
postLength = []
for d in data:
	authorList.append(d['author'])
	numpost = numpost+1

	initPost = d['title']
	if 'selftext' in d.keys():
		initPost = initPost+' '+d['selftext']

	postLength.append(len( initPost.split(' ') ))
	if d['comments']:
		for c in d['comments']:
			authorList.append(c['data'][0]['author'])
			numpost = numpost+1
			cText = c['data'][0]['body']
			postLength.append(len( cText.split(' ') ))

print('num post including comments:',numpost)
print('average post length:', sum(postLength)/float(numpost))
print('all users including comments:',len(set(authorList)))

#commentList = []
#userList = []
#for d in dataTobacco:
#	userList.append(d['author'])
#	commentList.append(d['num_comments'])
	

#pickle.dump(commentList, open('tobacco_submissionComment_2013-2018.p','wb'))
#pickle.dump(userList,open('cessation_submissionUser_2013-2018.p','wb'))

