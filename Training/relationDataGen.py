#!../../anaconda2/bin/python

import os
import reader
import itertools
import spacy
from gensim.models.doc2vec import Doc2Vec
from gensim.models import Word2Vec
import numpy as np

#load spacy english model
nlp = spacy.load("en_core_web_sm")

#load doc2vec
doc2vecModel = Doc2Vec.load('/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/enwiki_dbow/doc2vec.bin')

#load word2vec
word2vecModel = Word2Vec.load("/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/word2vec.bin")

#annotation data and corpus data
dirAdj = "RelationshipData/Adjudication/"
dirCorpus = "RelationshipData/Corpus/"

#classes label
relationClasses = [
'COMBUST_MJ_TO_COMBUST_TOBACCO',
'COMBUST_MJ_TO_SMOKING_CESSATION',
'COMBUST_MJ_TO_VAPING',
'COMBUST_MJ_TO_VAPING_MJ',
'COMBUST_MJ_TO_VAPING_NIC',
'COMBUST_TOBACCO_TO_COMBUST_MJ',
'COMBUST_TOBACCO_TO_SMOKING_CESSATION',
'COMBUST_TOBACCO_TO_VAPING',
'COMBUST_TOBACCO_TO_VAPING_MJ',
'COMBUST_TOBACCO_TO_VAPING_NIC/TOBACCO',
'COUSE_TO_SMOKING_CESSATION',
'DUAL_COMBUST_MJ_TOBACCO_TO_SMOKING_CESSATION',
'DUAL_COMBUST_MJ_VAPE_NIC_TO_SMOKING_CESSATION',
'DUAL_COMBUST_MJ_VAPING_MJ_TO_SMOKING_CESSATION',
'DUAL_COMBUST_TOBACCO_VAPING_NIC_TO_SMOKING_CESSATION',
'DUAL_VAPING_MJ_COMBUST_TOBACCO_TO_SMOKING_CESSATION',
'DUAL_VAPING_MJ_NIC_TO_SMOKING_CESSATION',
'POLY_COMBUST_MJ_VAPING MJ_NIC_TO_SMOKING_CESSATION',
'POLY_COMBUST_TOBACCO_MJ_VAPING_MJ_TO_SMOKING_CESSATION',
'POLY_COMBUST_TOBACCO_MJ_VAPING_NIC_TO_SMOKING_CESSATION',
'POLY_COMBUST_TOBACCO_VAPING_MJ_NIC_TO_SMOKING_CESSATION',
'VAPING_MJ_TO_COMBUST_MJ',
'VAPING_MJ_TO_COMBUST_TOBACCO',
'VAPING_MJ_TO_SMOKING_CESSATION',
'VAPING_MJ_TO_VAPING',
'VAPING_MJ_TO_VAPING_NIC',
'VAPING_NIC_TO_COMBUST_MJ',
'VAPING_NIC_TO_COMBUST_TOBACCO',
'VAPING_NIC_TO_SMOKING_CESSATION',
'VAPING_NIC_TO_VAPING',
'VAPING_NIC_TO_VAPING_MARIJUANA',
'VAPING_TO_COMBUST_MJ',
'VAPING_TO_COMBUST_TOBACCO',
'VAPING_TO_SMOKING_CESSATION',
'VAPING_TO_VAPING_MJ',
'VAPING_TO_VAPING_NIC',
' '
]

dataList = []
labelList = []
#form data instances
for annotFile in os.listdir(dirAdj):
	#print(annotFile)
	anotDicList = reader.annotFileReader_relationship(dirAdj+annotFile)
	corpusData = reader.corpusFileReader(dirCorpus+annotFile.replace('.knowtator.xml',''))
	print(annotFile,"num annot:", len(anotDicList))
	#parse get token and POS
        doc = nlp(corpusData.decode('UTF8'))

	#get POS for each annotation
	#find POS for annotation word
	for x in doc:
		for annot in anotDicList:
			if min(annot['end'], x.idx+len(x.text)-1)-max(annot['start'],x.idx) >0:
				annot['POS'] = x.pos #int format

				try:
					annot['previous_1'] = x.nbor(-1)
					annot['previous_1_POS'] = x.nbor(-1).pos
				except IndexError:
					annot['previous_1'] = x
                                        annot['previous_1_POS'] = x.pos
					annot['previous_2'] = x
					annot['previous_2_POS'] = x.pos
				try:
					annot['previous_2'] = x.nbor(-2)
					annot['previous_2_POS'] = x.nbor(-2).pos
				except IndexError:
					try:
						annot['previous_2'] = x.nbor(-1)
						annot['previous_2_POS'] = x.nbor(-1).pos
					except IndexError:
						annot['previous_2'] = x
						annot['previous_2_POS'] = x.pos

				try:
					annot['next_1'] = x.nbor(1)
					annot['next_1_POS'] = x.nbor(1).pos
				except IndexError:
					annot['next_1'] = x
					annot['next_1_POS'] = x.pos
					annot['next_2'] = x
					annot['next_2_POS'] = x.pos
				try:
					annot['next_2'] = x.nbor(2)
					annot['next_2_POS'] = x.nbor(2).pos
				except IndexError:
					try:
						annot['next_2'] = x.nbor(1)
						annot['next_2_POS'] = x.nbor(1).pos
					except IndexError:
						annot['previous_2'] = x
						annot['previous_2_POS'] = x.pos
#	for a in anotDicList:
#		print('---------')
#		print(a)
		
	#arbitary pair of annotation
	instanceList = []
	numRelation = 0
	for pair in itertools.permutations(anotDicList,2):
		numRelation = numRelation+1
		#range of pair for phrase: only phrase has reading direction
		minWordStart = min(pair[0]['start'], pair[1]['start'])
		maxWordEnd = max(pair[0]['end'], pair[1]['end'])
		#phrase and start and end words 300
		if pair[0]['start'] ==minWordStart:
			phraseStart = pair[0]['previous_2'].idx
		else:
			phraseStart = pair[1]['previous_2'].idx
		if pair[0]['end'] ==maxWordEnd:
                        phraseEnd = pair[0]['next_2'].idx
                else:
                        phraseEnd = pair[1]['next_2'].idx
	
		phraseString = corpusData[phraseStart:phraseEnd]
		phraseDoc = nlp(phraseString.decode('UTF8'))
		phraseWordList = []
		for w in phraseDoc:
			phraseWordList.append(w.text)
		phraseVector = doc2vecModel.infer_vector(phraseWordList)		

		#word vector word2vecModel 300
		try:
			wordStartVector = word2vecModel.wv[pair[0]['spannedText']]#[wordStart]
		except KeyError:
			wordStartVector = np.zeros(300)
		try:
			wordEndVector = word2vecModel.wv[pair[1]['spannedText']]#[wordEnd]
		except KeyError:
			wordEndVector = np.zeros(300) 

		#POS tag vector for start and end words
		POSvector = np.array([pair[0]['POS'],pair[1]['POS']])

		#for each relationship label for vector #it doesn't matter direction, as the permutation pairs includes all direction.
		if pair[0]['relationList']:
			for r in pair[0]['relationList']:
				if r['refID'] == pair[1]['AnnotID']: #there is one annotation from startAnnot to endAnnot
					relation = r['relation']
					dataVector = np.hstack((phraseVector,wordStartVector,wordEndVector, POSvector))
					dataList.append(dataVector)
					labelList.append(relation)
		else:
			relation = ' '
			dataVector = np.hstack((phraseVector,wordStartVector,wordEndVector, POSvector))
			dataList.append(dataVector)
			labelList.append(relation)
	print("number of pair relation:",numRelation)

print('size data sample:',len(dataList),len(labelList))		

import pickle
pickle.dump(dataList, open( "relationDataVectorList.p", "wb" ) )	
pickle.dump(labelList, open( "relationDataLabelList.p", "wb" ) )
pickle.dump(relationClasses,open("relationAllCategoryList.p","wb"))
