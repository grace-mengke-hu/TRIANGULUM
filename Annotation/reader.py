
#return list of  dictionary format annotations
def annotFileReader(filename):
	#parse xml
	import xml.etree.ElementTree as ET 
	xmlTree = ET.parse(filename)
	root = xmlTree.getroot()

	anotDicList = []
	n = 0
	for child in root.iter('annotation'):
		n = n+1
		anotDicList.append({})

	i=0
	while(i<n):
		for child in root:
			if child.tag == 'annotation':
				i = i+1
				anotDicList[i-1]['mentionSlot'] = []
				anotDicList[i-1]['stringSlotMentionValue'] = []	

			for c in child:
				if c.tag == 'spannedText':
					anotDicList[i-1]['spannedText'] = c.text
				if c.tag == 'span':
					anotDicList[i-1]['start'] = int(c.attrib['start'])
					anotDicList[i-1]['end'] = int(c.attrib['end'])
				if c.tag == 'mentionClass':#attribute class
					anotDicList[i-1]['class'] = c.attrib['id']
				if c.tag == 'mentionSlot':#attribute name
					anotDicList[i-1]['mentionSlot'].append(c.attrib['id'])
				if c.tag == 'stringSlotMentionValue':#attribute value
					if 'id' in c.attrib.keys():
						anotDicList[i-1]['stringSlotMentionValue'].append(c.attrib['id']) 

	return anotDicList


#return list of  dictionary format annotations including relationships
def annotFileReader_relationship(filename):
	#parse xml
	import xml.etree.ElementTree as ET 
	xmlTree = ET.parse(filename)
	root = xmlTree.getroot()

	#initialize new annotation (relationship embeded)
	anotDicList = []
	n = 0
	for child in root.iter('annotation'):
		n = n+1
		anotDicList.append({})
	
	#collect information for each annotation
	i=0
	while(i<n):
		for child in root:
			#initialize new annotation and collect basic information
			if child.tag == 'annotation':
				#initialize
				i = i+1
				anotDicList[i-1]['mentionSlot'] = [] #attribute list
				anotDicList[i-1]['stringSlotMentionValue'] = [] #attribute mention list
				anotDicList[i-1]['relationList'] = [] #relationship list
				#collect basic annotation info
				for c in child:
					if c.tag == 'mention':
						anotDicList[i-1]['AnnotID'] = c.attrib['id']
					if c.tag == 'spannedText':
						anotDicList[i-1]['spannedText'] = c.text
					if c.tag == 'span':
						anotDicList[i-1]['start'] = int(c.attrib['start'])
						anotDicList[i-1]['end'] = int(c.attrib['end'])
					#if c.tag == 'mentionClass':#class
					#	anotDicList[i-1]['class'] = c.attrib['id']

			#classMention
			if child.tag == 'classMention':
				for c in child:
					if c.tag == 'mentionClass':#class
						anotDicList[i-1]['class'] = c.attrib['id']
			#Attribute
			if child.tag == 'stringSlotMention': 
				for c in child:
					if c.tag == 'mentionSlot':#attribute name
						anotDicList[i-1]['mentionSlot'].append(c.attrib['id'])
					if c.tag == 'stringSlotMentionValue':#attribute value
						if 'id' in c.attrib.keys():#maybe no value
							anotDicList[i-1]['stringSlotMentionValue'].append(c.attrib['id'])  

			#Relationships
			if child.tag == 'complexSlotMention':
				tmpDic = {}
				tmpDic['attrib'] = []
				tmpDic['attribVal'] = []
				for c in child:
					if c.tag == 'mentionSlot':
						tmpDic['relation'] = c.attrib['id']
					if c.tag == 'attribute':
						tmpDic['attrib'].append(c.attrib['id'])
						tmpDic['attribVal'].append(c.text)
					if c.tag == 'complexSlotMentionValue':
						tmpDic['refID'] = c.attrib['value']
				anotDicList[i-1]['relationList'].append(tmpDic)
					
	return anotDicList


#return string from txt file
def corpusFileReader(filename):
	with open(filename, 'r') as file:
		data = file.read()
	return data

