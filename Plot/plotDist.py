#!../../anaconda2/bin/python
import pickle
import UnixTime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from collections import Counter


timeList = pickle.load(open("tobacco_submissionUTC_2013-2018.p","rb"))
userList = pickle.load(open("tobacco_submissionUser_2013-2018.p","rb"))
numCommentList = pickle.load(open("tobacco_submissionComment_2013-2018.p","rb"))
monthlyBin = UnixTime.monthlyTimeList()
yearlyLabel = UnixTime.yearlyLabelList()

#subplot
fig, axs = plt.subplots(2, 3)#2 row 3 column

#plot post volum by month
timePosts = np.asarray(timeList)
Bin = np.asarray(monthlyBin)
counts, bins, patches = axs[0, 0].hist(timePosts,bins=Bin,color='blue',histtype=u'step')#, density=True)
	#axs[0, 0].set_title('post volumn by month')
#axs[0,0].ticklabel_format(style='plain')
axs[0, 0].set(xlabel = 'Year',ylabel='Post Count')
axs[0,0].set_xlim([1356998401,1546300798])
axs[0,0].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
yearLabel = ['2013','2014','2015','2016','2017','2018']
labels = [item.get_text() for item in axs[0,0].get_xticklabels()]         
for i in range(len(labels)):
        labels[i] = yearLabel[i]           
axs[0,0].set_xticklabels(labels)


#plot user volumn by month
numUserInBinList = []
for i in range(len(monthlyBin)-1):
	currentBinUsers = set()
	for j in range(len(timeList)):
		if timeList[j]>=monthlyBin[i] and timeList[j]<=monthlyBin[i+1]:
			currentBinUsers.add(userList[j])
	numUserInBinList.append(len(currentBinUsers))

axs[0,1].plot(np.array(monthlyBin[0:len(monthlyBin)-1]),np.array(numUserInBinList),'blue')
axs[0,1].set(xlabel = 'Year',ylabel='User Count')
axs[0,1].set_xlim([1356998401,1546300798])
axs[0,1].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
yearLabel = ['2013','2014','2015','2016','2017','2018']
labels = [item.get_text() for item in axs[0,1].get_xticklabels()]         
for i in range(len(labels)):
        labels[i] = yearLabel[i]           
axs[0,1].set_xticklabels(labels)


#plot user tenure dist
userTimeDic = {}
for i in range(len(userList)):
	if userList[i] in userTimeDic.keys():
		userTimeDic[userList[i]].append(timeList[i])
	else: #first time reach this user/initialization
		userTimeDic[userList[i]] = []
		userTimeDic[userList[i]].append(timeList[i])
tenureList = []
for u in userTimeDic.keys():
	postTimes = userTimeDic[u]
	tenureList.append((max(postTimes)-min(postTimes))/float(2419201) ) #30 days
tenureBin = np.arange(0,72,1)
counts, bins, patches = axs[0, 2].hist(np.array(tenureList),bins=tenureBin,color='skyblue')
#axs[0,2].ticklabel_format(style='plain')
axs[0,2].set(xlabel = 'Tenure(months)',ylabel='User count')
axs[0,2].set_xlim([0,40])
axs[0,2].set_xticks(np.arange(0,35,5))
monthLabel = ['0','5','10','15','20','25','30','35']
labels = [item.get_text() for item in axs[0,2].get_xticklabels()]         
for i in range(len(labels)):
	labels[i] = monthLabel[i]          
axs[0,2].set_xticklabels(labels)


#plot user initiating post
userDist = Counter(userList).values()
initBin = np.arange(0,30,1)
counts, bins, patches = axs[1, 0].hist(np.array(userDist),bins = initBin,color='skyblue')
#axs[1,0].ticklabel_format(style='plain')
axs[1,0].set(xlabel = 'Initiating posts per user',ylabel='User count')
axs[1,0].set_xlim([0,40])
#axs[1,0].set_xticklabels(fontsize=12)




#user response post
userResponseDic = {}
for i in range(len(userList)):
	if userList[i] in userResponseDic.keys():	
		userResponseDic[userList[i]].append(numCommentList[i])
	else:
		userResponseDic[userList[i]] = []
		userResponseDic[userList[i]].append(numCommentList[i])
responsePerUser = []
for u in userResponseDic.keys():
	responsePerUser.append(sum(userResponseDic[u]))
#plt.hist(responsePerUser)
responseBin = np.arange(0,30,1)
counts, bins, patches = axs[1, 1].hist(np.array(responsePerUser),bins = responseBin,color='skyblue')
#axs[1,1].ticklabel_format(style='plain')
axs[1,1].set(xlabel = 'Responses per user',ylabel='User count')
#axs[1,1].set_xlim([0,40])
#axs[1,1].set_xticklabels(fontsize=12)


##thread length 
commentBin = np.arange(0,50,1)
print(numCommentList[0:10])
counts, bins, patches = axs[1, 2].hist(np.array(numCommentList),bins = commentBin,color='skyblue')
#plt.hist(numCommentList)
#axs[1,2].ticklabel_format(style='plain')
axs[1,2].set(xlabel = 'Thread length (#posts)',ylabel='Thread count')
#axs[1,2].set_xticklabels(fontsize=12)

plt.subplots_adjust(wspace = 0.3,hspace = 0.3)
	
	
	

plt.show()

