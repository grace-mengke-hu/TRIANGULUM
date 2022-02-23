#!../anaconda2/bin/python
import pickle

#load juul pickle
juul_Vaping101 = pickle.load( open( "JuulTrend/juul_Vaping101_utc.p", "rb" ) )
juul_vaping = pickle.load( open( "JuulTrend/juul_vaping_utc.p", "rb" ) )
juul_trees = pickle.load( open( "JuulTrend/juul_trees_utc.p", "rb" ) )
juul_stopsmoking = pickle.load( open( "JuulTrend/juul_stopsmoking_utc.p", "rb" ) )
juul_marijuana = pickle.load( open( "JuulTrend/juul_marijuana_utc.p", "rb" ) )
juul_electronic_cigarette = pickle.load( open( "JuulTrend/juul_electronic_cigarette_utc.p", "rb" ) )
juul_Cigarettes = pickle.load( open( "JuulTrend/juul_Cigarettes_utc.p", "rb" ) )

#load suorin pickle
suorin_Vaping101 = pickle.load( open( "JuulTrend/suorin_Vaping101_utc.p", "rb" ) )
suorin_vaping = pickle.load( open( "JuulTrend/suorin_vaping_utc.p", "rb" ) )
suorin_trees = pickle.load( open( "JuulTrend/suorin_trees_utc.p", "rb" ) )
suorin_stopsmoking = pickle.load( open( "JuulTrend/suorin_stopsmoking_utc.p", "rb" ) )
suorin_electronic_cigarette = pickle.load( open( "JuulTrend/suorin_electronic_cigarette_utc.p", "rb" ) )
suorin_Cigarettes = pickle.load( open( "JuulTrend/suorin_Cigarettes_utc.p", "rb" ) )

#load phix pickle
phix_trees = pickle.load( open( "JuulTrend/phix_trees_utc.p", "rb" ) )
phix_vaping = pickle.load( open( "JuulTrend/phix_vaping_utc.p", "rb" ) )
phix_stopsmoking = pickle.load( open( "JuulTrend/phix_stopsmoking_utc.p", "rb" ) )
phix_electronic_cigarette = pickle.load( open( "JuulTrend/phix_electronic_cigarette_utc.p", "rb" ) )
phix_Cigarettes = pickle.load( open( "JuulTrend/phix_Cigarettes_utc.p", "rb" ) )

#allUTC = juul_Vaping101+juul_vaping+juul_trees+juul_stopsmoking+juul_marijuana+juul_electronic_cigarette+juul_Cigarettes
#allUTC = suorin_Vaping101+suorin_vaping+suorin_trees+suorin_stopsmoking+suorin_electronic_cigarette+suorin_Cigarettes
allUTC = phix_trees+phix_vaping+phix_stopsmoking+phix_electronic_cigarette+phix_Cigarettes
print(allUTC[0:10])

#get the bin for monthly time stamps
monthlyBin = [	1356998400, #0:0:0 1/1/2013
		1359676800, #0:0:0 2/1/2013
		1362096000, #0:0:0 3/1/2013
		1364774400, #0:0:0 4/1/2013
		1367366400, #0:0:0 5/1/2013
		1370044800, #0:0:0 6/1/2013
		1372636800, #0:0:0 7/1/2013
		1375315200, #0:0:0 8/1/2013
		1377993600, #0:0:0 9/1/2013
		1380585600, #0:0:0 10/1/2013
		1383264000, #0:0:0 11/1/2013
		1385856000, #0:0:0 12/1/2013
		1388534400, #0:0:0 1/1/2014
		1391212800, #0:0:0 2/1/2014
		1393632000, #0:0:0 3/1/2014
		1396310400, #0:0:0 4/1/2014
		1398902400, #0:0:0 5/1/2014
		1401580800, #0:0:0 6/1/2014
		1404172800, #0:0:0 7/1/2014
		1406851200, #0:0:0 8/1/2014
		1409529600, #0:0:0 9/1/2014
		1412121600, #0:0:0 10/1/2014
		1414800000, #0:0:0 11/1/2014
		1417392000, #0:0:0 12/1/2014
		1420070400, #0:0:0 1/1/2015
		1422748800, #0:0:0 2/1/2015
		1425168000, #0:0:0 3/1/2015
		1427846400, #0:0:0 4/1/2015
		1430438400, #0:0:0 5/1/2015
		1433116800, #0:0:0 6/1/2015
		1435708800, #0:0:0 7/1/2015
		1438387200, #0:0:0 8/1/2015
		1441065600, #0:0:0 9/1/2015
		1443657600, #0:0:0 10/1/2015
		1446336000, #0:0:0 11/1/2015
		1448928000, #0:0:0 12/1/2015
		1451606400, #0:0:0 1/1/2016
		1454284800, #0:0:0 2/1/2016
		1456790400, #0:0:0 3/1/2016
		1459468800, #0:0:0 4/1/2016
		1462060800, #0:0:0 5/1/2016
		1464739200, #0:0:0 6/1/2016
		1467331200, #0:0:0 7/1/2016
		1470009600, #0:0:0 8/1/2016
		1472688000, #0:0:0 9/1/2016
		1475280000, #0:0:0 10/1/2016
		1477958400, #0:0:0 11/1/2016
		1480550400, #0:0:0 12/1/2016
		1483228800, #0:0:0 1/1/2017
		1485907200, #0:0:0 2/1/2017
		1488326400, #0:0:0 3/1/2017
		1491004800, #0:0:0 4/1/2017
		1493596800, #0:0:0 5/1/2017
		1496275200, #0:0:0 6/1/2017
		1498867200, #0:0:0 7/1/2017
		1501545600, #0:0:0 8/1/2017
		1504224000, #0:0:0 9/1/2017
		1506816000, #0:0:0 10/1/2017
		1509494400, #0:0:0 11/1/2017
		1512086400, #0:0:0 12/1/2017
		1514764800, #0:0:0 1/1/2018
		1517443200, #0:0:0 2/1/2018
		1519862400, #0:0:0 3/1/2018
		1522540800, #0:0:0 4/1/2018
		1525132800, #0:0:0 5/1/2018
		1527811200, #0:0:0 6/1/2018
		1530403200, #0:0:0 7/1/2018
		1533081600, #0:0:0 8/1/2018
		1535760000, #0:0:0 9/1/2018
		1538352000, #0:0:0 10/1/2018
		1541030400, #0:0:0 11/1/2018
		1543622399 #23:59:59 11/30/2018
]

xAxis = ['1-1-13',
'2-1-13',
'3-1-13',
'4-1-13',
'5-1-13',
'6-1-13',
'7-1-13',
'8-1-13',
'9-1-13',
'10-1-13',
'11-1-13',
'12-1-13',
'1-1-14',
'2-1-14',
'3-1-14',
'4-1-14',
'5-1-14',
'6-1-14',
'7-1-14',
'8-1-14',
'9-1-14',
'10-1-14',
'11-1-14',
'12-1-14',
'1-1-15',
'2-1-15',
'3-1-15',
'4-1-15',
'5-1-15',
'6-1-15',
'7-1-15',
'8-1-15',
'9-1-15',
'10-1-15',
'11-1-15',
'12-1-15',
'1-1-16',
'2-1-16',
'3-1-16',
'4-1-16',
'5-1-16',
'6-1-16',
'7-1-16',
'8-1-16',
'9-1-16',
'10-1-16',
'11-1-16',
'12-1-16',
'1-1-17',
'2-1-17',
'3-1-17',
'4-1-17',
'5-1-17',
'6-1-17',
'7-1-17',
'8-1-17',
'9-1-17',
'10-1-17',
'11-1-17',
'12-1-17',
'1-1-18',
'2-1-18',
'3-1-18',
'4-1-18',
'5-1-18',
'6-1-18',
'7-1-18',
'8-1-18',
'9-1-18',
'10-1-18',
'11-1-18',
'11-30-18'
]
import numpy as np

UTCs = np.asarray(allUTC)
Bin = np.asarray(monthlyBin)
#UTCsorted = np.sort(UTCs)

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
fig, ax = plt.subplots()
#plt.xlim(xmin = 1356998399,xmax = 1543622400)
counts, bins, patches = ax.hist(UTCs, bins=monthlyBin)
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
