#!../../anaconda2/bin/python
import pickle
import label
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from collections import Counter
import UnixTime

labelDic = label.classLabel()
monthlyBin = UnixTime.monthlyTimeList()

#cessation
timeLabelDic_c = pickle.load(open("cessation_timeLSTMcatDicSimple_2013-2018.p","rb"))
#tobacco
timeLabelDic_t = pickle.load(open("tobacco_timeLSTMcatDicSimple_2013-2018.p","rb"))
#marijuana
timeLabelDic_m = pickle.load(open("MJ_timeLSTMcatDicSimple_2013-2018.p","rb"))
#vaping
timeLabelDic_v = pickle.load(open("vaping_timeLSTMcatDicSimple_2013-2018.p","rb"))

#'VAPING_MJ','VAPING_NIC','COMBUST_MJ','COMBUST_TOBACCO','CESSATION'

#---vaping MJ
#tobacco
vapingMJ_t = []
for t in timeLabelDic_t.keys():
	if 'VAPING_MJ' in timeLabelDic_t[t]:
		vapingMJ_t.append(t)
#vaping
vapingMJ_v = []
for t in timeLabelDic_v.keys():
	if 'VAPING_MJ' in timeLabelDic_v[t]:
		vapingMJ_v.append(t)
#marijuana
vapingMJ_m = []
for t in timeLabelDic_m.keys():
	if 'VAPING_MJ' in timeLabelDic_m[t]:
		vapingMJ_m.append(t)
#cessation
vapingMJ_c = []
for t in timeLabelDic_c.keys():
	if 'VAPING_MJ' in timeLabelDic_c[t]:
		vapingMJ_c.append(t)

#---vapingNic
#cessation
vapingNic_c = []
for t in timeLabelDic_c.keys():
	if 'VAPING_NIC' in timeLabelDic_c[t]:
		vapingNic_c.append(t)
#tobacco
vapingNic_t = []
for t in timeLabelDic_t.keys():
	if 'VAPING_NIC' in timeLabelDic_t[t]:
		vapingNic_t.append(t)
#vaping
vapingNic_v = []
for t in timeLabelDic_v.keys():
	if 'VAPING_NIC' in timeLabelDic_v[t]:
		vapingNic_v.append(t)
#marijuana
vapingNic_m = []
for t in timeLabelDic_m.keys():
	if 'VAPING_NIC' in timeLabelDic_m[t]:
		vapingNic_m.append(t)

#---combustible MJ
#cessation
combustMJ_c = []
for t in timeLabelDic_c.keys():
	if 'COMBUST_MJ' in timeLabelDic_c[t]:
		combustMJ_c.append(t)
#vaping
combustMJ_v = []
for t in timeLabelDic_v.keys():
	if 'COMBUST_MJ' in timeLabelDic_v[t]:
		combustMJ_v.append(t)
#marijuana
combustMJ_m = []
for t in timeLabelDic_m.keys():
	if 'COMBUST_MJ' in timeLabelDic_m[t]:
		combustMJ_m.append(t)
#tobacco
combustMJ_t = []
for t in timeLabelDic_t.keys():
	if 'COMBUST_MJ' in timeLabelDic_t[t]:
		combustMJ_t.append(t)

#---combustible tobacco
#cessation
combustT_c = []
for t in timeLabelDic_c.keys():
	if 'COMBUST_TOBACCO' in timeLabelDic_c[t]:
		combustT_c.append(t)
#vaping
combustT_v = []
for t in timeLabelDic_v.keys():
	if 'COMBUST_TOBACCO' in timeLabelDic_v[t]:
		combustT_v.append(t)
#marijuana
combustT_m = []
for t in timeLabelDic_m.keys():
	if 'COMBUST_TOBACCO' in timeLabelDic_m[t]:
		combustT_m.append(t)
#tobacco
combustT_t = []
for t in timeLabelDic_t.keys():
	if 'COMBUST_TOBACCO' in timeLabelDic_t[t]:
		combustT_t.append(t)

#---cessation concepts
#tobacco
cessation_t = []
for t in timeLabelDic_t.keys():
        if 'CESSATION' in timeLabelDic_t[t]:
                cessation_t.append(t)
#marijuana
cessation_m = []
for t in timeLabelDic_m.keys():
	if 'CESSATION' in timeLabelDic_m[t]:
		cessation_m.append(t)
#vaping
cessation_v = []
for t in timeLabelDic_v.keys():
	if 'CESSATION' in timeLabelDic_v[t]:
		cessation_v.append(t)
#cessation
cessation_c = []
for t in timeLabelDic_c.keys():
	if 'CESSATION' in timeLabelDic_c[t]:
		cessation_c.append(t)

#plot figures
Bin = np.asarray(monthlyBin)
yearLabel = ['2013','2014','2015','2016','2017','2018']
BinYear = np.asarray([  1356998400, #0:0:0 1/1/2013
                1388534400, #0:0:0 1/1/2014
                1420070400, #0:0:0 1/1/2015
                1451606400, #0:0:0 1/1/2016
                1483228800, #0:0:0 1/1/2017
                1514764800, #0:0:0 1/1/2018
                1546300799, #23:59:59 12/31/2018
])

fig, axs = plt.subplots(2,3)#,figsize=(15,15))
#tobacco concepts (forums time trend)
counts, bins, patches = axs[0,0].hist([vapingMJ_t,vapingMJ_v,vapingMJ_m,vapingMJ_c], bins=BinYear,color=['darkcyan','lightgreen','sandybrown','cornflowerblue'],label=['Tobacco','ENDS','Marijuana','Cessation'])
axs[0,0].set(xlabel = 'Year',ylabel='#post in vaping MJ.')
axs[0,0].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[0,0].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = yearLabel[i]
axs[0,0].set_xticklabels(labels)
axs[0,0].legend(loc="upper left")

#vaping concepts (forums time trend)
counts, bins, patches = axs[0,1].hist([vapingNic_t,vapingNic_v,vapingNic_m,vapingNic_c], bins=BinYear,color=['darkcyan','lightgreen','sandybrown','cornflowerblue'],label=['Tobacco','ENDS','Marijuana','Cessation'])
axs[0,1].set(xlabel = 'Year',ylabel='#post in vaping nic.')
axs[0,1].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[0,1].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = yearLabel[i]
axs[0,1].set_xticklabels(labels)
axs[0,1].legend(loc="upper left")

#combustible tobacco concepts (forums time trend)
counts, bins, patches = axs[0,2].hist([combustT_t,combustT_v,combustT_m,combustT_c], bins=BinYear,color=['darkcyan','lightgreen','sandybrown','cornflowerblue'],label=['Tobacco','ENDS','Marijuana','Cessation'])
axs[0,2].set(xlabel = 'Year',ylabel='#post in combust. tobacco')
axs[0,2].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[0,2].get_xticklabels()]
for i in range(len(labels)):	
	labels[i] = yearLabel[i]
axs[0,2].set_xticklabels(labels)
axs[0,2].legend(loc="upper left")

#combustible MJ concept
counts, bins, patches = axs[1,0].hist([combustMJ_t,combustMJ_v,combustMJ_m,combustMJ_c], bins=BinYear,color=['darkcyan','lightgreen','sandybrown','cornflowerblue'],label=['Tobacco','ENDS','Marijuana','Cessation'])
axs[1,0].set(xlabel = 'Year',ylabel='#post in combust. MJ')
axs[1,0].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[1,0].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = yearLabel[i]
axs[1,0].set_xticklabels(labels)
axs[1,0].legend(loc="upper left")


#cessation concepts (forums time trend)
counts, bins, patches = axs[1,2].hist([cessation_t,cessation_v,cessation_m,cessation_c], bins=BinYear,color=['darkcyan','lightgreen','sandybrown','cornflowerblue'],label=['Tobacco','ENDS','Marijuana','Cessation'])
axs[1,2].set(xlabel = 'Year',ylabel='#post in cessation')
axs[1,2].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[1,2].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = yearLabel[i]
axs[1,2].set_xticklabels(labels)
axs[1,2].legend(loc="upper left")



plt.delaxes(axs[1,1])


#plt.subplots_adjust(hspace = 1.0)



plt.show()





