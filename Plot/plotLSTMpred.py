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
timeLabelDic_c = pickle.load(open("cessation_timeLSTMcatDic_2013-2018.p","rb"))
#tobacco
timeLabelDic_t = pickle.load(open("tobacco_timeLSTMcatDic_2013-2018.p","rb"))
#marijuana
timeLabelDic_m = pickle.load(open("MJ_timeLSTMcatDic_2013-2018.p","rb"))
#vaping
timeLabelDic_v = pickle.load(open("vaping_timeLSTMcatDic_2013-2018.p","rb"))


#---vaping concepts
#tobacco
vaping_t = []
for t in timeLabelDic_t.keys():
	if 'VAPING' in timeLabelDic_t[t]:
		vaping_t.append(t)
#vaping
vaping_v = []
for t in timeLabelDic_v.keys():
	if 'VAPING' in timeLabelDic_v[t]:
		vaping_v.append(t)
#marijuana
vaping_m = []
for t in timeLabelDic_m.keys():
	if 'VAPING' in timeLabelDic_m[t]:
		vaping_m.append(t)
#cessation
vaping_c = []
for t in timeLabelDic_c.keys():
	if 'VAPING' in timeLabelDic_c[t]:
		vaping_c.append(t)

#---tobacco concepts
#cessation
tobacco_c = []
for t in timeLabelDic_c.keys():
	if 'TOBACCO' in timeLabelDic_c[t]:
		tobacco_c.append(t)
#tobacco
tobacco_t = []
for t in timeLabelDic_t.keys():
	if 'TOBACCO' in timeLabelDic_t[t]:
		tobacco_t.append(t)
#vaping
tobacco_v = []
for t in timeLabelDic_v.keys():
	if 'TOBACCO' in timeLabelDic_v[t]:
		tobacco_v.append(t)
#marijuana
tobacco_m = []
for t in timeLabelDic_m.keys():
	if 'TOBACCO' in timeLabelDic_m[t]:
		tobacco_m.append(t)

#---marijuana concepts
#cessation
marijuana_c = []
for t in timeLabelDic_c.keys():
	if 'MJ' in timeLabelDic_c[t]:
		marijuana_c.append(t)
#vaping
marijuana_v = []
for t in timeLabelDic_v.keys():
	if 'MJ' in timeLabelDic_v[t]:
		marijuana_v.append(t)
#marijuana
marijuana_m = []
for t in timeLabelDic_m.keys():
	if 'MJ' in timeLabelDic_m[t]:
		marijuana_m.append(t)
#tobacco
marijuana_t = []
for t in timeLabelDic_t.keys():
	if 'MJ' in timeLabelDic_t[t]:
		marijuana_t.append(t)

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

fig, axs = plt.subplots(2,2)
#tobacco concepts (forums time trend)
counts, bins, patches = axs[0,0].hist(tobacco_t, bins=Bin,color='darkcyan',histtype=u'step',label="Tobacco")
counts, bins, patches = axs[0,0].hist(tobacco_v, bins=Bin,color='lightgreen',histtype=u'step',label="ENDS")
counts, bins, patches = axs[0,0].hist(tobacco_m, bins=Bin,color='sandybrown',histtype=u'step',label="Marijuana")
counts, bins, patches = axs[0,0].hist(tobacco_c, bins=Bin,color='cornflowerblue',histtype=u'step',label="Cessation")
axs[0,0].set(xlabel = 'Year',ylabel='tobacco concept post count')
axs[0,0].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[0,0].get_xticklabels()]
for i in range(len(labels)):
	labels[i] = yearLabel[i]
axs[0,0].set_xticklabels(labels)
axs[0,0].legend(loc="upper right")

#vaping concepts (forums time trend)
counts, bins, patches = axs[0,1].hist(vaping_t, bins=Bin,color='darkcyan',histtype=u'step',label="Tobacco")
counts, bins, patches = axs[0,1].hist(vaping_v, bins=Bin,color='lightgreen',histtype=u'step',label="ENDS")
counts, bins, patches = axs[0,1].hist(vaping_m, bins=Bin,color='sandybrown',histtype=u'step',label="Marijuana")
counts, bins, patches = axs[0,1].hist(vaping_c, bins=Bin,color='cornflowerblue',histtype=u'step',label="Cessation")
axs[0,1].set(xlabel = 'Year',ylabel='vaping concept post count')
axs[0,1].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[0,1].get_xticklabels()]
for i in range(len(labels)):
        labels[i] = yearLabel[i]
axs[0,1].set_xticklabels(labels)
axs[0,1].legend(loc="upper right")

#marijuana concepts (forums time trend)
counts, bins, patches = axs[1,0].hist(marijuana_t, bins=Bin,color='darkcyan',histtype=u'step',label="Tobacco")
counts, bins, patches = axs[1,0].hist(marijuana_v, bins=Bin,color='lightgreen',histtype=u'step',label="ENDS")
counts, bins, patches = axs[1,0].hist(marijuana_m, bins=Bin,color='sandybrown',histtype=u'step',label="Marijuana")
counts, bins, patches = axs[1,0].hist(marijuana_c, bins=Bin,color='cornflowerblue',histtype=u'step',label="Cessation")
axs[1,0].set(xlabel = 'Year',ylabel='marijuana concept post count')
axs[1,0].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[1,0].get_xticklabels()]
for i in range(len(labels)):
        labels[i] = yearLabel[i]
axs[1,0].set_xticklabels(labels)
axs[1,0].legend(loc="upper right")

#cessation concepts (forums time trend)
counts, bins, patches = axs[1,1].hist(cessation_t, bins=Bin,color='darkcyan',histtype=u'step',label="Tobacco")
counts, bins, patches = axs[1,1].hist(cessation_v, bins=Bin,color='lightgreen',histtype=u'step',label="ENDS")
counts, bins, patches = axs[1,1].hist(cessation_m, bins=Bin,color='sandybrown',histtype=u'step',label="Marijuana")
counts, bins, patches = axs[1,1].hist(cessation_c, bins=Bin,color='cornflowerblue',histtype=u'step',label="Cessation")
axs[1,1].set(xlabel = 'Year',ylabel='cessation concept post count')
axs[1,1].set_xticks(np.array([1372636800,1404172800,1435708800,1467331200,1498867200,1530403200]))
labels = [item.get_text() for item in axs[1,1].get_xticklabels()]
for i in range(len(labels)):
        labels[i] = yearLabel[i]
axs[1,1].set_xticklabels(labels)
axs[1,1].legend(loc="upper right")











plt.show()





