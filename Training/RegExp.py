##!../../anaconda2/bin/python

##import re

#category:regExp
tobaccoDic = {
'nic':"(\W|^)nic(\W|$)|(\W|^)nicotine(\W|$)",
'tobacco':"(\W|^)tobacco(\W|$)|(\W|^)tabacco(\W|$)|(\W|^)tobbaco(\W|$)|(\W|^)tobaco(\W|$)|(\W|^)tobacoo(\W|$)|(\W|^)tobbacco(\W|$)|(\W|^)tabaco(\W|$)|(\W|^)tabbaco(\W|$)|(\W|^)tobaccoo(\W|$)|(\W|^)tabbacco(\W|$)",
'cig':"(\W|^)cigarette(\W|$)|(\W|^)cigarettes(\W|$)|(\W|^)cig(\W|$)|(\W|^)cigs(\W|$)|(\W|^)ciggs(\W|$)|(\W|^)cigg(\W|$)|(\W|^)ciggarettes(\W|$)|(\W|^)ciggarette(\W|$)|(\W|^)cigarette(\W|$)|(\W|^)cigarettes(\W|$)|(\W|^)cig(\W|$)|(\W|^)cigs(\W|$)",
'smoke':"(\W|^)smoking(\W|$)|(\W|^)smoke(\W|$)|(\W|^)smoked(\W|$)|(\W|^)smokes(\W|$)",
'cigar':"(\W|^)cigar(\W|$)|(\W|^)cigars(\W|$)",
'bidis':"(\W|^)bidis(\W|$)",
'roll-your-own':"(\W|^)roll\Wyour\Wown(\W|$)|(\W|^)ryo(\W|$)|(\W|^)roll\syour\sown(\W|$)",
'roll-up':"(\W|^)roll\Wup(\W|$)|(\W|^)roll\Wups(\W|$)|(\W|^)roll\sups(\W|$)|(\W|^)roll\sup(\W|$)",
'hand-rolled-cigarettes':"(\W|^)hand\Wrolled\Wcigarettes(\W|$)|(\W|^)hrc(\W|$)|(\W|^)hand\Wrolled\Wcigarette(\W|$)|(\W|^)hand\Wrolled\scigarette(\W|$)|(\W|^)hand\Wrolled\scigarettes(\W|$)",
'blunt':"(\W|^)blunts(\W|$)|(\W|^)blunt(\W|$)",
'hookah':"(\W|^)hookah(\W|$)|(\W|^)hookahs(\W|$)|(\W|^)hooka(\W|$)|(\W|^)hookas(\W|$)",
'shisha':"(\W|^)shisha(\W|$)",
'narghile':"(\W|^)narghile(\W|$)",
'water pipe':"(\W|^)water\spipe(\W|$)|(\W|^)water\Wpipe(\W|$)",
'baccy':"(\W|^)baccy(\W|$)",
'greengo':"(\W|^)greengo(\W|$)",
'tabacum':"(\W|^)tabacum(\W|$)",
'cigarillos':"(\W|^)cigarillos(\W|$)|(\W|^)cigarillo(\W|$)",
'flue':"(\W|^)flue(\W|$)",
'damiana':"(\W|^)damiana(\W|$)",
'dokha':"(\W|^)dokha(\W|$)",
'latakia':"(\W|^)latakia(\W|$)",
'mullein':"(\W|^)mullein(\W|$)",
'snus':"(\W|^)snus(\W|$)",
'clove':"(\W|^)cloves(\W|$)|(\W|^)clove(\W|$)",
'syo':"(\W|^)syo(\W|$)",
'spliff':"(\W|^)splifs(\W|$)|(\W|^)splif(\W|$)|(\W|^)spliffs(\W|$)|(\W|^)spliff(\W|$)",
'diacetyl':"(\W|^)diacetyl(\W|$)",
'rustica':"(\W|^)rustica(\W|$)",
'xtraslo':"(\W|^)xtraslo(\W|$)",
'cannabis':"(\W|^)cannabis(\W|$)",
'thuoc':"(\W|^)thuoc(\W|$)",
'dutchmaster':"(\W|^)dutchmaster(\W|$)",
'hemp':"(\W|^)hemp(\W|$)",
'burley':"(\W|^)burley(\W|$)",
'tobac':"(\W|^)tobac(\W|$)",
'macanudo':"(\W|^)macanudo(\W|$)",
'cavendish':"(\W|^)cavendish(\W|$)",
'knaster':"(\W|^)knaster(\W|$)",
'cigarellos':"(\W|^)cigarellos(\W|$)",
'wta':"(\W|^)wta(\W|$)",
'acetaldehyde':"(\W|^)acetaldehyde(\W|$)",
'decarboxylated':"(\W|^)decarboxylated(\W|$)",
'rolling tobacco':"(\W|^)rolling\stobacco(\W|$)"
}


marijuanaDic = {
'marijuana':"(\W|^)marijuana(\W|$)|(\W|^)marujuana(\W|$)|(\W|^)mari(\W|$)|(\W|^)matijuana(\W|$)|(\W|^)marjuana(\W|$)|(\W|^)marjiuana(\W|$)|(\W|^)marinuana(\W|$)|(\W|^)marijauana(\W|$)|(\W|^)marijunna(\W|$)|(\W|^)marijana(\W|$)|(\W|^)marijuna(\W|$)|(\W|^)marihuana(\W|$)|(\W|^)marijauna(\W|$)|(\W|^)marijuanna(\W|$)|(\W|^)marajuana(\W|$)|(\W|^)mj(\W|$)|(\W|^)mmj(\W|$)",
'weed':"(\W|^)weed(\W|$)",
#'spliff':"(\W|^)spliff(\W|$)|(\W|^)spliffs(\W|$)|(\W|^)splifs(\W|$)|(\W|^)splif(\W|$)",
'skunk':"(\W|^)skunk(\W|$)",
'hash':"(\W|^)hash(\W|$)",
'pot':"(\W|^)pot(\W|$)",
'cannabis':"(\W|^)cannabis(\W|$)|(\W|^)cannibis(\W|$)|(\W|^)cannibas(\W|$)|(\W|^)cannibus(\W|$)|(\W|^)cannibinoids(\W|$)|(\W|^)canniboids(\W|$)|(\W|^)cannbis(\W|$)|(\W|^)canabis(\W|$)|(\W|^)cannabidiol(\W|$)|(\W|^)cannabinoids(\W|$)|(\W|^)canabinoids(\W|$)|(\W|^)cannabinoid(\W|$)|(\W|^)cannaboids(\W|$)|(\W|^)cannabanoids(\W|$)|(\W|^)cannabanoid(\W|$)|(\W|^)canabinoids(\W|$)|(\W|^)canabinoid(\W|$)",
'hemp':"(\W|^)hemp(\W|$)",
'tree':"(\W|^)trees(\W|$)|(\W|^)tree(\W|$)",
'blunt':"(\W|^)blunts(\W|$)|(\W|^)blunt(\W|$)",
#'smok':"(\W|^)smoking(\W|$)|(\W|^)smoke(\W|$)|(\W|^)smoked(\W|$)|(\W|^)smokes(\W|$)",
'bong':"(\W|^)bong(\W|$)|(\W|^)bongs(\W|$)",
'toke':"(\W|^)toke(\W|$)|(\W|^)toking(\W|$)|(\W|^)toked(\W|$)",
'joint':"(\W|^)joint(\W|$)|(\W|^)joints(\W|$)",
'420':"(\W|^)(420)(\W|$)",
'mulls':"(\W|^)mulls(\W|$)",
'cbd':"(\W|^)cbds(\W|$)|(\W|^)cbd(\W|$)|(\W|^)cbda(\W|$)",
'cbns':"(\W|^)cbns(\W|$)",
'cbg':"(\W|^)cbg(\W|$)",
'THC':"(\W|^)thca(\W|$)|(\W|^)thc(\W|$)|(\W|^)cooh(\W|$)|(\W|^)thc\scooh(\W|$)",
'cooh':"(\W|^)cooh(\W|$)",
'marijuanatar':"(\W|^)marijuanatar(\W|$)",
'pethidine':"(\W|^)pethidine(\W|$)",
'acetaldehyde':"(\W|^)acetaldehyde(\W|$)",
'decarboxylated':"(\W|^)decarboxylated(\W|$)",
'lipophilic':"(\W|^)lipophilic(\W|$)",
'roll-your-own':"(\W|^)roll\Wyour\Wown(\W|$)|(\W|^)ryo(\W|$)",
'roll-up':"(\W|^)roll\Wup(\W|$)|(\W|^)roll\Wups(\W|$)",
'syo':"(\W|^)syo(\W|$)",
'mcigs':"(\W|^)mcigs(\W|$)|(\W|^)mcig(\W|$)",
'bowl':"(\W|^)bowl(\W|$)|(\W|^)bowls(\W|$)",
'stoned':"(\W|^)stoned(\W|$)|(\W|^)stone(\W|$)",
'kief':"(\W|^)kief(\W|$)",
'bud':"(\W|^)bud(\W|$)"
}

vapeDic = {
'vaping':"(\W|^)vaping(\W|$)|(\W|^)vapeing(\W|$)",
'tank':"(\W|^)tank(\W|$)",
'electronic cigarette':"(\W|^)electronic\scigarette(\W|$)|(\W|^)electronic\scigarettes(\W|$)|(\W|^)ecig(\W|$)|(\W|^)ecigs(\W|$)|(\W|^)e\scig(\W|$)|(\W|^)e\scigs(\W|$)|(\W|^)e\Wcig(\W|$)|(\W|^)e\Wcigs(\W|$)|(\W|^)ecigarette(\W|$)|(\W|^)ecigarettes(\W|$)|(\W|^)e\scigarette(\W|$)|(\W|^)e\scigarettes(\W|$)|(\W|^)e\Wcigarette(\W|$)|(\W|^)e\Wcigarettes(\W|$)",
'e-hookah':"(\W|^)e\Whookah(\W|$)|(\W|^)e\Whookahs(\W|$)|(\W|^)e\Whooka(\W|$)|(\W|^)e\Whookas(\W|$)",
'vape pen':"(\W|^)vape\spen(\W|$)|(\W|^)vape\spens(\W|$)",
'e-liquid':"(\W|^)e\Wliquid(\W|$)|(\W|^)e\sliquid(\W|$)",
'e-juice':"(\W|^)e\Wjuice(\W|$)|(\W|^)e\sjuice(\W|$)",
'JUUL':"(\W|^)JUULING(\W|$)|(\W|^)JUULS(\W|$)|(\W|^)JUUL(\W|$)|(\W|^)juuling(\W|$)|(\W|^)juuls(\W|$)|(\W|^)juul(\W|$)",
'Sourin':"(\W|^)Sourin(\W|$)|(\W|^)sourin(\W|$)|(\W|^)suorin(\W|$)",
'mod':"(\W|^)mod(\W|$)|(\W|^)mods(\W|$)",
'hookah pen':"(\W|^)hookah\spen(\W|$)|(\W|^)hookah\spens(\W|$)",
'juice':"(\W|^)juice(\W|$)",
'vaporizer':"(\W|^)vaporizer(\W|$)",
'atomizer':"(\W|^)atomizer(\W|$)",
'charger':"(\W|^)charger(\W|$)",
'battery':"(\W|^)battery(\W|$)",
'kanger':"(\W|^)kanger(\W|$)",
'cartomizer':"(\W|^)cartomizer(\W|$)",
'cartridge':"(\W|^)cartridge(\W|$)",
'cigalike':"(\W|^)cigalike(\W|$)",
'PV':"(\W|^)pv(\W|$)",
'APV':"(\W|^)apv(\W|$)",
'atty':"(\W|^)atty(\W|$)",
'carto':"(\W|^)carto(\W|$)",
'cart':"(\W|^)cart(\W|$)",
'coil':"(\W|^)coil(\W|$)",
'PG':"(\W|^)pg(\W|$)",
'VG':"(\W|^)vg(\W|$)",
'tanklet':"(\W|^)tanklet(\W|$)",
'charm':"(\W|^)charm(\W|$)",
'DCT':"(\W|^)dct(\W|$)",
'passthr':"(\W|^)passthrough(\W|$)|(\W|^)passthru(\W|$)",
'vapor':"(\W|^)vapor(\W|$)|(\W|^)vapour(\W|$)|(\W|^)vape(\W|$)|(\W|^)vapes(\W|$)|(\W|^)vaping(\W|$)|(\W|^)vaped(\W|$)|(\W|^)vapourizer(\W|$)|(\W|^)vaporizer(\W|$)|(\W|^)vaporiser(\W|$)|(\W|^)vapouriser(\W|$)|(\W|^)vaporization(\W|$)|(\W|^)vapourization(\W|$)|(\W|^)vapourisation(\W|$)|(\W|^)vaporisation(\W|$)|(\W|^)vaporization(\W|$)|(\W|^)vapourize(\W|$)|(\W|^)vapourise(\W|$)|(\W|^)vaporize(\W|$)|(\W|^)vaporise(\W|$)|(\W|^)vapourized(\W|$)|(\W|^)vapourised(\W|$)|(\W|^)vaporized(\W|$)|(\W|^)vaporised(\W|$)|(\W|^)vap(\W|$)|(\W|^)vaps(\W|$)",
'volcano':"(\W|^)volcano(\W|$)",
'herb':"(\W|^)herb(\W|$)",
'brand':"(\W|^)mflb(\W|$)|(\W|^)portable(\W|$)|(\W|^)pax(\W|$)|(\W|^)wax(\W|$)|(\W|^)solo(\W|$)|(\W|^)stiiizy(\W|$)|(\W|^)gpen(\W|$)",
'dab':"(\W|^)dab(\W|$)|(\W|^)dabs(\W|$)|(\W|^)dabbing(\W|$)",
'concentrate':"(\W|^)concentrates(\W|$)|(\W|^)concentrate(\W|$)",
'shisha':"(\W|^)shisha(\W|$)",
'cartridge':"(\W|^)cartridges(\W|$)|(\W|^)cartridge(\W|$)",
'flowermate':"(\W|^)flowermate(\W|$)",
'dynavap':"(\W|^)dynavap(\W|$)",
'tfn':"(\W|^)tfn(\W|$)",
'enano':"(\W|^)enano(\W|$)",
'tabletop':"(\W|^)tabletop(\W|$)",
'vapcap':"(\W|^)vapcap(\W|$)",
'vaporbrothers':"(\W|^)vaporbrothers(\W|$)|(\W|^)vaporbrother(\W|$)",
'rig':"(\W|^)rig(\W|$)",
'wta':"(\W|^)wta(\W|$)",
'tinh':"(\W|^)tinh(\W|$)",
'whip':"(\W|^)whip(\W|$)",
'apx':"(\W|^)apx(\W|$)",
'extremeq':"(\W|^)extremeq(\W|$)",
'mcigs':"(\W|^)mcigs(\W|$)|(\W|^)mcig(\W|$)",
'cart':"(\W|^)carts(\W|$)|(\W|^)cart(\W|$)|(\W|^)carto(\W|$)",
'arizer':"(\W|^)arizer(\W|$)",
'phix':"(\W|^)phix(\W|$)",
'vaporent':"(\W|^)vaporents(\W|$)|(\W|^)vaporents(\W|$)",
'ritchy':"(\W|^)ritchy(\W|$)",
'vapium':"(\W|^)vapium(\W|$)",
'ssv':"(\W|^)ssv(\W|$)",
'dbv':"(\W|^)dbv(\W|$)",
'firefly':"(\W|^)firefly(\W|$)",
'IQOS':"(\W|^)IQOS(\W|$)|(\W|^)iqos(\W|$)",
'mflb':"(\W|^)mflb(\W|$)|(\W|^)MFLB(\W|$)",
'abv':"(\W|^)abv(\W|$)|(\W|^)ABV(\W|$)",
'shatter':"(\W|^)shatter(\W|$)",
'quit':"(\W|^)quit(\W|$)"
}
# add all regex dic together
tobaccoDic.update(marijuanaDic)
tobaccoDic.update(vapeDic)
allDic = tobaccoDic.copy()

#rule based:
rules={
'CO-USE_COMBUST_MJ_COMBUST_TOBACCO':['blunt','spliff'],

'DUAL-USE_COMBUST_MJ_VAPING_MJ':[],

'DUAL-USE_COMBUST_MJ_VAPE_NIC/TOBACCO':[],

'DUAL-USE_COMBUST_MJ_COMBUST_TOBACCO':[],

'DUAL-USE_VAPING_MJ_VAPING_NIC/TOBACCO':[],

'DUAL-USE_COMBUST_TOBACCO_VAPING_NIC/TOBACCO':[],

'DUAL-USE_VAPING_MJ_COMBUST_TOBACCO':[],

'POLY-USE_COMBUST_TOBACCO_COMBUST_MJ_VAPING_MJ':[],

'POLY-USE_COMBUST_TOBACCO_COMBUST_MJ_VAPING_NIC/TOBACCO':[],

'POLY_USE_COMBUST_TOABBCO_VAPING_MJ_VAPING_NIC/TOBACCO':[],

'POLY_USE_COMBUST_MJ_VAPING_MJ_VAPING_NIC/TOBACCO':[],

'COMBUST_MJ':['bud','abv','kief','stoned','blunt','marijuana','weed','spliff','skunk','hash','pot','cannabis','hemp','tree','blunt','smoke','bong','toke','joint','420','mulls','cbd','cbns','cbg','THC','cooh','marijuanatar','pethidine','acetaldehyde','decarboxylated','lipophilic','roll-your-own','roll-up','syo','mcigs','bowl'],

'COMBUST_TOBACCO':['nic','tobacco','cig','smoke','cigar','bidis','roll-your-own','roll-up','hand-rolled-cigarettes','blunt','hookah','shisha','narghile','water pipe','baccy','greengo','tabacum','cigarillos','flue','damiana','dokha','latakia','mullein','snus','clove','syo','spliff','rustica','xtraslo','cannabis','thuoc','dutchmaster','hemp','burley','tobac','macanudo','cavendish','knaster','cigarellos','wta','acetaldehyde','decarboxylated','rolling tobacco'],

'VAPING_MJ':['dab','herb','abv','shatter'],

'VAPING_NIC/TOBACCO':['IQOS','vaping','tank','electronic cigarette','e-hookah','vape pen','e-liquid','e-juice','JUUL','Sourin','mod','hookah pen','juice','vaporizer','atomizer','charger','battery','kanger','cartomizer','cartridge','cigalike','PV','APV','atty','carto','cart','coil','PG','VG','tanklet','charm','DCT','passthr','vapor','concentrate','shisha','cartridge','rig','tinh','whip','cart'],

'BRAND':['mflb','volcano','brand','flowermate','dynavap','tfn','enano','tabletop','vapcap','vaporbrothers','wta','apx','extremeq','mcigs','arizer','phix','vaporent','ritchy','vapium','ssv','dbv','firefly'],

'VAPING':['greengo'],

'SMOKING_CESSATION':['quit']

}

#word: cat list dictionary
rulesWordDic = {}
for cat in rules.keys():
	 for word in rules[cat]:
		if word in rulesWordDic.keys():
			rulesWordDic[word].append(cat)
		else:
			rulesWordDic[word] = []
			rulesWordDic[word].append(cat)

def regExDetect(docString):
	import re
	Annot = []
	#for each keyword match in document
	for keyword in allDic.keys():
		if re.search(allDic[keyword],docString) != None: #find it
			matchObjList = re.finditer(allDic[keyword],docString)
			for obj in matchObjList:
				#get category
				catList = rulesWordDic[keyword]
				#build annotations
				for cat in catList:
					tmpDic = {}
					tmpDic['category'] = cat
					tmpDic['wordText'] = obj.group()
					tmpDic['start'] = obj.start()
					tmpDic['end'] = obj.end()
					Annot.append(tmpDic)
	return Annot


def regExDetect_subreddit(docString,subreddit):
	import re
	Annot = []
	#for each keyword match in document
	for keyword in allDic.keys():
		if re.search(allDic[keyword],docString) != None: #find it
			matchObjList = re.finditer(allDic[keyword],docString)
			for obj in matchObjList:
				#get category
				if keyword =='smoke':
					if subreddit in ['trees','weed','marijuana','marijuanaenthusiast']:
						tmpDic = {}
						tmpDic['category'] = 'COMBUST_MJ'
						tmpDic['wordText'] = obj.group()
						tmpDic['start'] = obj.start()
						tmpDic['end'] = obj.end()
						Annot.append(tmpDic)
					elif subreddit in ['cigarette','Cigarette','cigarettes','Cigarettes']:
						tmpDic = {}
						tmpDic['category'] ='COMBUST_TOBACCO' 
						tmpDic['wordText'] = obj.group()
						tmpDic['start'] = obj.start()
						tmpDic['end'] = obj.end()
						Annot.append(tmpDic)
					else:
						tmpDic = {}
						tmpDic['category'] = 'VAPING_NIC/TOBACCO'
						tmpDic['wordText'] = obj.group()
						tmpDic['start'] = obj.start()
						tmpDic['end'] = obj.end()
						Annot.append(tmpDic)
				else:
					catList = rulesWordDic[keyword]
					#build annotations
					for cat in catList:
						tmpDic = {}
						tmpDic['category'] = cat
						tmpDic['wordText'] = obj.group()
						tmpDic['start'] = obj.start()
						tmpDic['end'] = obj.end()
						Annot.append(tmpDic)
	return Annot


#testString = "cig i smoke "+'\n\n'+"bong every day.smoke 420"

#annot = regExDetect(testString)
#print(annot)
#print(allDic['420'])
