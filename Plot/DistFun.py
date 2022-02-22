#!../../anaconda2/bin/python
import pickle
import UnixTime

monthlyBin = UnixTime.monthlyTimeList()
timeList = pickle.load(open("cessation_submissionUTC_2013-2018.p","rb"))
userList = pickle.load(open("cessation_submissionUser_2013-2018.p","rb"))
numCommentList = pickle.load(open("cessation_submissionComment_2013-2018.p","rb"))


BinYearList = [  1356998400, #0:0:0 1/1/2013
                1388534400, #0:0:0 1/1/2014
                1420070400, #0:0:0 1/1/2015
                1451606400, #0:0:0 1/1/2016
                1483228800, #0:0:0 1/1/2017
                1514764800, #0:0:0 1/1/2018
                1546300799, #23:59:59 12/31/2018
]
#------user volumn by month
numUserInBinList = []
for i in range(len(BinYearList)-1):
	currentBinUsers = set()
	for j in range(len(timeList)):
		if timeList[j]>=BinYearList[i] and timeList[j]<=BinYearList[i+1]:
			currentBinUsers.add(userList[j])
	numUserInBinList.append(len(currentBinUsers))
pickle.dump(numUserInBinList,open('cessation_numUserInBinListYear.p','wb'))



##plot user tenure dist
#userTimeDic = {}
#for i in range(len(userList)):
#	if userList[i] in userTimeDic.keys():
#		userTimeDic[userList[i]].append(timeList[i])
#	else: #first time reach this user/initialization
#		userTimeDic[userList[i]] = []
#		userTimeDic[userList[i]].append(timeList[i])
#tenureList = []
#for u in userTimeDic.keys():
#	postTimes = userTimeDic[u]
#	tenureList.append((max(postTimes)-min(postTimes))/float(2419201) ) #30 days
#pickle.dump(tenureList,open('tobacco_tenureList.p','wb'))

##user response post
#userResponseDic = {}
#for i in range(len(userList)):
#	if userList[i] in userResponseDic.keys():
#		userResponseDic[userList[i]].append(numCommentList[i])
#	else:
#		userResponseDic[userList[i]] = []
#		userResponseDic[userList[i]].append(numCommentList[i])
#responsePerUser = []
#for u in userResponseDic.keys():
#		responsePerUser.append(sum(userResponseDic[u]))	
#pickle.dump(responsePerUser,open('tobacco_responsePerUser.p','wb'))
