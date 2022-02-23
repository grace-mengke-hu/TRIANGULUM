#!../anaconda2/bin/python
import pickle

#load juul pickle
juul_Vaping101 = pickle.load( open( "JuulTrend/juul_Vaping101_2013-2018_utc.p", "rb" ) )
juul_vaping = pickle.load( open( "JuulTrend/juul_vaping2013-2018_utc.p", "rb" ) )
juul_trees = pickle.load( open( "JuulTrend/juul_trees_2013-2018_utc.p", "rb" ) )
juul_stopsmoking = pickle.load( open( "JuulTrend/juul_stopsmoking2013-2018_utc.p", "rb" ) )
juul_marijuana = pickle.load( open( "JuulTrend/juul_marijuana2013-2018_utc.p", "rb" ) )
juul_electronic_cigarette = pickle.load( open( "JuulTrend/juul_e_cig2013-2018_utc.p", "rb" ) )
juul_Cigarettes = pickle.load( open( "JuulTrend/juul_cig2013-2018_utc.p", "rb" ) )
juul_MJen = pickle.load( open( "JuulTrend/juul_marijuanaEnthusiast2013-2018_utc.p", "rb" ) )
juul_weed = pickle.load( open( "JuulTrend/juul_weed2013-2018_utc.p", "rb" ) )

#load suorin pickle
suorin_Vaping101 = pickle.load( open( "JuulTrend/suorin_Vaping101_2013-2018_utc.p", "rb" ) )
suorin_vaping = pickle.load( open( "JuulTrend/suorin_vaping2013-2018_utc.p", "rb" ) )
suorin_trees = pickle.load( open( "JuulTrend/suorin_trees_2013-2018_utc.p", "rb" ) )
suorin_stopsmoking = pickle.load( open( "JuulTrend/suorin_stopsmoking2013-2018_utc.p", "rb" ) )
suorin_marijuana = pickle.load( open( "JuulTrend/suorin_marijuana2013-2018_utc.p", "rb" ) )
suorin_electronic_cigarette = pickle.load( open( "JuulTrend/suorin_e_cig2013-2018_utc.p", "rb" ) )
suorin_Cigarettes = pickle.load( open( "JuulTrend/suorin_cig2013-2018_utc.p", "rb" ) )
suorin_MJen = pickle.load( open( "JuulTrend/suorin_marijuanaEnthusiast2013-2018_utc.p", "rb" ) )
suorin_weed = pickle.load( open( "JuulTrend/suorin_weed2013-2018_utc.p", "rb" ) )

#load phix pickle
phix_trees = pickle.load( open( "JuulTrend/phix_trees_2013-2018_utc.p", "rb" ) )
phix_vaping = pickle.load( open( "JuulTrend/phix_vaping2013-2018_utc.p", "rb" ) )
phix_stopsmoking = pickle.load( open( "JuulTrend/phix_stopsmoking2013-2018_utc.p", "rb" ) )
phix_electronic_cigarette = pickle.load( open( "JuulTrend/phix_e_cig2013-2018_utc.p", "rb" ) )
phix_Cigarettes = pickle.load( open( "JuulTrend/phix_cig2013-2018_utc.p", "rb" ) )
phix_marijuana = pickle.load( open( "JuulTrend/phix_marijuana2013-2018_utc.p", "rb" ) )
phix_MJen = pickle.load( open( "JuulTrend/phix_marijuanaEnthusiast2013-2018_utc.p", "rb" ) )
phix_Vaping101 = pickle.load( open( "JuulTrend/phix_Vaping101_2013-2018_utc.p", "rb" ) )
phix_weed = pickle.load( open( "JuulTrend/phix_weed2013-2018_utc.p", "rb" ) )

allUTCjuul = juul_Vaping101+juul_vaping+juul_trees+juul_stopsmoking+juul_marijuana+juul_electronic_cigarette+juul_Cigarettes+juul_MJen+juul_weed
allUTCsuorin = suorin_Vaping101+suorin_vaping+suorin_trees+suorin_stopsmoking+suorin_electronic_cigarette+suorin_Cigarettes+suorin_MJen+suorin_weed+suorin_marijuana
allUTCphix = phix_trees+phix_vaping+phix_stopsmoking+phix_electronic_cigarette+phix_Cigarettes+phix_marijuana+phix_MJen+phix_Vaping101+phix_weed

#get the bin for monthly time stamps
monthlyBin = [	1356998400, #0:0:0 1/1/2013
		1388534400, #0:0:0 1/1/2014
		1420070400, #0:0:0 1/1/2015
		1451606400, #0:0:0 1/1/2016
		1483228800, #0:0:0 1/1/2017
		1514764800, #0:0:0 1/1/2018
		1546300799, #23:59:59 12/31/2018
]

xAxis = ['1-1-13',
'1-1-14',
'1-1-15',
'1-1-16',
'1-1-17',
'1-1-18',
'12-31-18'
]
import numpy as np

UTCjuul = np.asarray(allUTCjuul)
UTCsuorin = np.asarray(allUTCsuorin)
UTCphix = np.asarray(allUTCphix)
#UTCs = np.stack((UTCjuul,UTCsuorin,UTCphix), axis=1)

Bin = np.asarray(monthlyBin)
#UTCsorted = np.sort(UTCs)

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
fig, ax = plt.subplots()
#plt.xlim(xmin = 1356998399,xmax = 1543622400)
counts, bins, patches = ax.hist([UTCjuul,UTCsuorin,UTCphix], bins=monthlyBin,color=['red','tan','lime'],label=['Juul', 'Suorin', 'Phix'])
ax.legend(prop={'size': 10})
ax.set_xticks(bins)
labels = [item.get_text() for item in ax.get_xticklabels()]

for i in range(len(labels)):
	labels[i] = xAxis[i]

ax.set_xticklabels(labels)
plt.xticks(rotation=45)
plt.show()
#plt.hist(UTCs, bins=monthlyBin)#,range=[1427000000, 1543622400])
##fig.canvas.draw()
#labels = [item.get_text() for item in ax.get_xticklabels()]
#print('label length:',len(labels),'date labe length',len(xAxis))
#plt.ylabel('Counts')
#plt.xlabel('UTC')
#plt.xticks(UTCs,xAxis,color='orange', rotation=45)
##plt.show()
