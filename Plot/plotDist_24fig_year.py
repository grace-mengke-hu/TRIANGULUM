#!../../anaconda2/bin/python
import pickle
import UnixTime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from collections import Counter

#monthly yearly bin
monthlyBin = UnixTime.monthlyTimeList()
yearlyLabel = UnixTime.yearlyLabelList()
#load cessation
timeList_c = pickle.load(open("cessation_submissionUTC_2013-2018.p","rb"))
userList_c = pickle.load(open("cessation_submissionUser_2013-2018.p","rb"))
numCommentList_c = pickle.load(open("cessation_submissionComment_2013-2018.p","rb"))
#load MJ
timeList_m = pickle.load(open("MJ_submissionUTC_2013-2018.p","rb"))
userList_m = pickle.load(open("MJ_submissionUser_2013-2018.p","rb"))
numCommentList_m = pickle.load(open("MJ_submissionComment_2013-2018.p","rb"))
#load tobacco
timeList_t = pickle.load(open("tobacco_submissionUTC_2013-2018.p","rb"))
userList_t = pickle.load(open("tobacco_submissionUser_2013-2018.p","rb"))
numCommentList_t = pickle.load(open("tobacco_submissionComment_2013-2018.p","rb"))
#load vaping
timeList_v = pickle.load(open("vaping_submissionUTC_2013-2018.p","rb"))
userList_v = pickle.load(open("vaping_submissionUser_2013-2018.p","rb"))
numCommentList_v = pickle.load(open("vaping_submissionComment_2013-2018.p","rb"))

BinYear = np.asarray([  1356998400, #0:0:0 1/1/2013
                1388534400, #0:0:0 1/1/2014
                1420070400, #0:0:0 1/1/2015
                1451606400, #0:0:0 1/1/2016
                1483228800, #0:0:0 1/1/2017
                1514764800, #0:0:0 1/1/2018
                1546300799, #23:59:59 12/31/2018
])

#subplot 24 figures
fig, axs = plt.subplots(4,6,figsize=(8,20))

#plot post volum by month
Bin = np.asarray(monthlyBin)
yearLabel = ['2013','2014','2015','2016','2017','2018']
timePosts_c = np.asarray(timeList_c)
timePosts_m = np.asarray(timeList_m)
timePosts_t = np.asarray(timeList_t)
timePosts_v = np.asarray(timeList_v) 
#tobacco
counts, bins, patches = axs[0,0].hist(timePosts_t, bins=BinYear,color='skyblue')#,histtype=u'step')
axs[0,0].set(xlabel = 'Year',ylabel='Post Count')
axs[0,0].set_ylim([0,150000])
axs[0,0].set_xlim([1356998401,1546300798])
axs[0,0].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200])) 
labels = [item.get_text() for item in axs[0,0].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = yearLabel[i]
axs[0,0].set_xticklabels(labels,rotation=45)
#vaping
counts, bins, patches = axs[1, 0].hist(timePosts_v, bins=BinYear,color='skyblue')#,histtype=u'step')
axs[1,0].set(xlabel = 'Year',ylabel='Post Count')
axs[1,0].set_ylim([0,150000])
axs[1,0].set_xlim([1356998401,1546300798])
axs[1,0].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[1,0].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = yearLabel[i]
axs[1,0].set_xticklabels(labels,rotation=45)
#marijuana
counts, bins, patches = axs[2,0].hist(timePosts_m, bins=BinYear,color='skyblue')#,histtype=u'step')
axs[2,0].set(xlabel = 'Year',ylabel='Post Count')
axs[2,0].set_ylim([0,150000])
axs[2,0].set_xlim([1356998401,1546300798])
axs[2,0].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[2,0].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = yearLabel[i]
axs[2,0].set_xticklabels(labels,rotation=45)
#cessation
counts, bins, patches = axs[3,0].hist(timePosts_c, bins=BinYear,color='skyblue')#,histtype=u'step')
axs[3,0].set(xlabel = 'Year',ylabel='Post Count')
axs[3,0].set_ylim([0,150000])
axs[3,0].set_xlim([1356998401,1546300798])
axs[3,0].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[3,0].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = yearLabel[i]
axs[3,0].set_xticklabels(labels,rotation=45)



#plot user volumn by month
numUserInBinList_c = pickle.load(open("cessation_numUserInBinListYear.p","rb"))
numUserInBinList_v = pickle.load(open("vaping_numUserInBinListYear.p","rb"))
numUserInBinList_m = pickle.load(open("MJ_numUserInBinListYear.p","rb"))
numUserInBinList_t = pickle.load(open("tobacco_numUserInBinListYear.p","rb"))
#tobacco
axs[0,1].plot(np.array(BinYear[0:len(BinYear)-1]),np.array(numUserInBinList_t),'blue')
axs[0,1].set(xlabel = 'Year',ylabel='User Count')
axs[0,1].set_ylim([0,55000])
axs[0,1].set_xlim([1356998401,1546300798])
axs[0,1].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[0,1].get_xticklabels()]         
for i in range(len(labels)):
	labels[i] = yearLabel[i]           
axs[0,1].set_xticklabels(labels,rotation=45)
#vaping
axs[1,1].plot(np.array(BinYear[0:len(BinYear)-1]),np.array(numUserInBinList_v),'blue')
axs[1,1].set(xlabel = 'Year',ylabel='User Count')
axs[1,1].set_ylim([0,55000])
axs[1,1].set_xlim([1356998401,1546300798])
axs[1,1].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[1,1].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = yearLabel[i]
axs[1,1].set_xticklabels(labels,rotation=45)
#marijuana
axs[2,1].plot(np.array(BinYear[0:len(BinYear)-1]),np.array(numUserInBinList_m),'blue')
axs[2,1].set(xlabel = 'Year',ylabel='User Count')
axs[2,1].set_ylim([0,55000])
axs[2,1].set_xlim([1356998401,1546300798])
axs[2,1].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[2,1].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = yearLabel[i]
axs[2,1].set_xticklabels(labels,rotation=45)
#cessation
axs[3,1].plot(np.array(BinYear[0:len(BinYear)-1]),np.array(numUserInBinList_c),'blue')
axs[3,1].set(xlabel = 'Year',ylabel='User Count')
axs[3,1].set_ylim([0,55000])
axs[3,1].set_xlim([1356998401,1546300798])
axs[3,1].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[3,1].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = yearLabel[i]
axs[3,1].set_xticklabels(labels,rotation=45)

#plot user tenure dist
tenureBin = np.arange(0,72,1)
tenureList_c = pickle.load(open("cessation_tenureList.p","rb"))
tenureList_t = pickle.load(open("tobacco_tenureList.p","rb"))
tenureList_m = pickle.load(open("MJ_tenureList.p","rb"))
tenureList_v = pickle.load(open("vaping_tenureList.p","rb"))
#tobacco
counts, bins, patches = axs[0,2].hist(np.array(tenureList_t),bins=tenureBin,color='skyblue')
median_t = np.median(np.array(counts))
#axs[0,2].spines['right'].set_position(('axes',median_t))
axs[0,2].set(xlabel = 'Tenure(months)',ylabel='User count')
axs[0,2].set_ylim([0,160000])
axs[0,2].set_xlim([0,2*median_t])
#print(median_t)
axs[0,2].set_xticks(np.arange(0,2*median_t,5))
monthLabel = ['0','5','10+']
#monthLabel = ['0','5','10','15','20','25','30','35']
labels = [item.get_text() for item in axs[0,2].get_xticklabels()]         
for i in range(len(labels)):
	labels[i] = monthLabel[i]          
axs[0,2].set_xticklabels(labels)
#vaping
counts, bins, patches = axs[1,2].hist(np.array(tenureList_v),bins=tenureBin,color='skyblue')
median_v = np.median(np.array(counts))
axs[1,2].set(xlabel = 'Tenure(months)',ylabel='User count')
axs[1,2].set_ylim([0,160000])
axs[1,2].set_xlim([0,6])
axs[1,2].set_xticks(np.arange(0,6,5))
print(median_v)
monthLabel = ['0','5+']
labels = [item.get_text() for item in axs[1,2].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = monthLabel[i]
axs[1,2].set_xticklabels(labels)
#marijuana
counts, bins, patches = axs[2,2].hist(np.array(tenureList_m),bins=tenureBin,color='skyblue')
axs[2,2].set(xlabel = 'Tenure(months)',ylabel='User count')
axs[2,2].set_ylim([0,160000])
axs[2,2].set_xlim([0,22])
axs[2,2].set_xticks(np.arange(0,22,5))
monthLabel = ['0','5','10','15','20+']
labels = [item.get_text() for item in axs[2,2].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = monthLabel[i]
axs[2,2].set_xticklabels(labels)
#cessation
counts, bins, patches = axs[3,2].hist(np.array(tenureList_c),bins=tenureBin,color='skyblue')
axs[3,2].set(xlabel = 'Tenure(months)',ylabel='User count')
axs[3,2].set_ylim([0,160000])
axs[3,2].set_xlim([0,45])
axs[3,2].set_xticks(np.arange(0,42,5))
monthLabel = ['0','5','10','15','20','25','30','35','40+']
labels = [item.get_text() for item in axs[3,2].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = monthLabel[i]
axs[3,2].set_xticklabels(labels)


#plot user initiating post
initBin = np.arange(0,30,1)
userDist_t = Counter(userList_t).values()
userDist_v = Counter(userList_v).values()
userDist_m = Counter(userList_m).values()
userDist_c = Counter(userList_c).values()
#tobacco
counts, bins, patches = axs[0, 3].hist(np.array(userDist_t),bins = initBin,color='skyblue')
axs[0,3].set(xlabel = 'Initiating posts per user',ylabel='User count')
axs[0,3].set_ylim([0,140000])
axs[0,3].set_xlim([0,10])
#vaping
counts, bins, patches = axs[1, 3].hist(np.array(userDist_v),bins = initBin,color='skyblue')
axs[1,3].set(xlabel = 'Initiating posts per user',ylabel='User count')
axs[1,3].set_ylim([0,140000])
axs[1,3].set_xlim([0,8])
#marijuana
counts, bins, patches = axs[2,3].hist(np.array(userDist_m),bins = initBin,color='skyblue')
axs[2,3].set(xlabel = 'Initiating posts per user',ylabel='User count')
axs[2,3].set_ylim([0,140000])
axs[2,3].set_xlim([0,15])
#cessation
counts, bins, patches = axs[3,3].hist(np.array(userDist_c),bins = initBin,color='skyblue')
axs[3,3].set(xlabel = 'Initiating posts per user',ylabel='User count')
axs[3,3].set_ylim([0,140000])
axs[3,3].set_xlim([0,30])


#user response post
responsePerUser_c = pickle.load(open("cessation_responsePerUser.p","rb"))
responsePerUser_m = pickle.load(open("MJ_responsePerUser.p","rb"))
responsePerUser_t = pickle.load(open("tobacco_responsePerUser.p","rb"))
responsePerUser_v = pickle.load(open("vaping_responsePerUser.p","rb"))
responseBin = np.arange(0,30,1)
#tobacco
counts, bins, patches = axs[0,4].hist(np.array(responsePerUser_t),bins = responseBin,color='skyblue')
axs[0,4].set_ylim([0,35000])
axs[0,4].set(xlabel = 'Responses per user',ylabel='User count')
#vaping
counts, bins, patches = axs[1,4].hist(np.array(responsePerUser_v),bins = responseBin,color='skyblue')
axs[1,4].set_ylim([0,35000])
axs[1,4].set(xlabel = 'Responses per user',ylabel='User count')
#marijuana
counts, bins, patches = axs[2,4].hist(np.array(responsePerUser_m),bins = responseBin,color='skyblue')
axs[2,4].set_ylim([0,35000])
axs[2,4].set(xlabel = 'Responses per user',ylabel='User count')
#cessation
counts, bins, patches = axs[3,4].hist(np.array(responsePerUser_c),bins = responseBin,color='skyblue')
axs[3,4].set_ylim([0,35000])
axs[3,4].set(xlabel = 'Responses per user',ylabel='User count')


#thread length 
commentBin = np.arange(0,50,1)
#tobacco
counts, bins, patches = axs[0,5].hist(np.array(numCommentList_t),bins = commentBin,color='skyblue')
axs[0,5].set_ylim([0,150000])
axs[0,5].set(xlabel = 'Thread length (#posts)',ylabel='Thread count')
#vaping
counts, bins, patches = axs[1,5].hist(np.array(numCommentList_v),bins = commentBin,color='skyblue')
axs[1,5].set_ylim([0,150000])
axs[1,5].set(xlabel = 'Thread length (#posts)',ylabel='Thread count')
#marijuana
counts, bins, patches = axs[2,5].hist(np.array(numCommentList_m),bins = commentBin,color='skyblue')
axs[2,5].set_ylim([0,150000])
axs[2,5].set(xlabel = 'Thread length (#posts)',ylabel='Thread count')
#cessation
counts, bins, patches = axs[3,5].hist(np.array(numCommentList_c),bins = commentBin,color='skyblue')
axs[3,5].set_ylim([0,150000])
axs[3,5].set(xlabel = 'Thread length (#posts)',ylabel='Thread count')

plt.subplots_adjust(wspace = 0.6,hspace = 0.6,bottom=0.1)#(bottom=0.1, right=0.8, top=0.9)
	
	
	

plt.show()

