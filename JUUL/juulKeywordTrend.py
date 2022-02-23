#!../anaconda2/bin/python
import json
import re


with open('../Data/weed2013-2018.json') as fp:
        data = json.load(fp)

print(data[0])

juulPattern = "(\W|^)juul(\W|$)|(\W|^)juuls(\W|$)|(\W|^)juuling(\W|$)|(\W|^)juuled(\W|$)|(\W|^)juuler(\W|$)"
suorinPattern = "(\W|^)suorin(\W|$)|(\W|^)suorins(\W|$)|(\W|^)suoren(\W|$)|(\W|^)suorens(\W|$)|(\W|^)suoran(\W|$)|(\W|^)suorans(\W|$)|(\W|^)sourin(\W|$)|(\W|^)sourins(\W|$)|(\W|^)souren(\W|$)|(\W|^)sourens(\W|$)|(\W|^)souran(\W|$)|(\W|^)sourans(\W|$)"
phixPattern = "(\W|^)phix(\W|$)"
#print(re.search(pattern,"juul consume suorin"))


textList = []
utcList = []
for sub in data:
	if 'selftext' in sub.keys():
		if re.search(suorinPattern, sub['title']+'\n\n'+sub['selftext'], re.IGNORECASE):
			textList.append(sub['title']+'\n\n'+sub['selftext'])
			utcList.append(sub['created_utc'])
	else:
		if re.search(suorinPattern,sub['title'],re.IGNORECASE):
			textList.append(sub['title'])
			utcList.append(sub['created_utc'])

	if sub['comments']:
		for c in sub['comments']:
			if re.search(suorinPattern,c['data'][0]['body'],re.IGNORECASE):
				#print(c['data'][0]['body'])
				textList.append(c['data'][0]['body'])
				utcList.append(c['data'][0]['created_utc'])	
#print(textList[0])


import pickle
pickle.dump(textList, open( "JuulTrend/suorin_weed2013-2018_text.p", "wb" ) )
pickle.dump(utcList, open( "JuulTrend/suorin_weed2013-2018_utc.p", "wb" ) )

