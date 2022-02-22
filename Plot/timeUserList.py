#!../../anaconda2/bin/python

import json
from collections import Counter
import pickle

##Tobacco
#with open("../../Data/cig2013-2018.json","r") as read_file:
#	dataTobacco = json.load(read_file)

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

#stop smoking
with open("../../Data/stopsmoking2013-2018.json","r") as read_file:
        dataCessation = json.load(read_file)


#Only submission: get list of users and list of time including repetition users and conflict time
timeList = []
userList = []
for d in dataCessation:
	timeList.append(d['created_utc'])
	userList.append(d['author'])

pickle.dump(timeList, open('cessation_submissionUTC_2013-2018.p','wb'))
pickle.dump(userList,open('cessation_submissionUser_2013-2018.p','wb'))

