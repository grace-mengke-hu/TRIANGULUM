#!../../anaconda2/bin/python

import pickle
import reader
import time
import spacy

#load spacy english model
nlp = spacy.load("en_core_web_sm")

#load feature data with filename
data1 = pickle.load( open( "4_10_findAnotData.p", "rb" ) )
data2 = pickle.load( open( "11_50_findAnotData.p", "rb" ) )
data3 = pickle.load( open( "51_100_findAnotData.p", "rb" ) )
data4 = pickle.load( open( "101_218_findAnotData.p", "rb" ) )
data5 = pickle.load( open( "218_1000_findAnotData.p", "rb" ) )

featData = data1+data2+data3+data4+data5

sentsTokenDic = {}
for d in featData:#[data1[0]]:#test on one sample
        corpusFilename = d['filename']
        parseList = corpusFilename.split('/')
        adjudicationFilename = '/'.join(parseList[0:-2])+'/Adjudication/'+parseList[-1]+'.knowtator.xml'
	print(corpusFilename)
	print(adjudicationFilename)
        subreddit = parseList[-1].split('_')[-1].replace('.txt','')
        #get corpus data and annotation data
        anotDicList = reader.annotFileReader_relationship(adjudicationFilename)
        corpusData = reader.corpusFileReader(corpusFilename)

	#NLP NER and Annotation
        doc = nlp(corpusData.decode('UTF8'))
	for x in doc:
		#search for the annotation for this token
                xStart = x.idx
                xEnd = x.idx+len(x.text)-1
                classLabel = ''
                for anot in anotDicList:
                        if min(anot['end'],xEnd)-max(anot['start'],xStart) >0:
                                classLabel = anot['class']

                if str(x.sent) in sentsTokenDic.keys():#REMARK: here str() is to convert any UTF8 char in string
                        sentsTokenDic[str(x.sent)].append((str(x).decode('utf-8', 'ignore'), x.pos_, x.ent_type_, classLabel.decode('utf-8') ))
		else:#new sentence
                        sentsTokenDic[str(x.sent)] = []

print(sentsTokenDic)   
print('number of sentences: ',len(sentsTokenDic))
	
#change sentence into numpy form
import numpy as np
sentences = []
sentence_pos = []
sentence_entity = []
sentence_annotClass = []
for sent in sentsTokenDic.keys():
	#print(sent)
	#print(sentsTokenDic[sent]) #some sentence key has empty token list []
	if sentsTokenDic[sent]:
		sentence,pos,entity,annotClass = zip(*sentsTokenDic[sent])
		#form np array list of sentences and tags
		sentences.append(np.array(sentence))
		sentence_pos.append(np.array(pos))
		sentence_entity.append(np.array(entity))
		sentence_annotClass.append(np.array(annotClass))
print(len(sentences))
#print(sentences[10]) 
#print(sentence_pos[10])
#print(sentence_entity[10])
#print(sentence_annotClass[10])

#split to train test
from sklearn.model_selection import train_test_split
(train_sentences, test_sentences, train_tags, test_tags) = train_test_split(sentences, sentence_annotClass, test_size=0.7)	

#before keras padding
words, tags = set([]), set([])
 
for s in sentences:
	for w in s:
		words.add(w.lower())
labels = ['','CO-USE_COMBUST_MJ_COMBUST_TOBACCO', 'DUAL-USE_COMBUST_MJ_VAPING_MJ', 'DUAL-USE_COMBUST_MJ_VAPE_NIC/TOBACCO', 'DUAL-USE_COMBUST_MJ_COMBUST_TOBACCO', 'DUAL-USE_VAPING_MJ_VAPING_NIC/TOBACCO','DUAL-USE_COMBUST_TOBACCO_VAPING_NIC/TOBACCO','DUAL-USE_VAPING_MJ_COMBUST_TOBACCO','POLY-USE_COMBUST_TOBACCO_COMBUST_MJ_VAPING_MJ','POLY-USE_COMBUST_TOBACCO_COMBUST_MJ_VAPING_NIC/TOBACCO','POLY_USE_COMBUST_TOABBCO_VAPING_MJ_VAPING_NIC/TOBACCO','POLY_USE_COMBUST_MJ_VAPING_MJ_VAPING_NIC/TOBACCO','COMBUST_MJ','COMBUST_TOBACCO','VAPING_MJ','VAPING_NIC/TOBACCO','BRAND','VAPING','SMOKING_CESSATION']

for ts in labels:
	tags.add(unicode(ts, "utf-8"))
#for s in train_sentences:
#	for w in s:
#		words.add(w.lower())
 
#for ts in train_tags:
#	for t in ts:
#		tags.add(t)
 
word2index = {w: i + 2 for i, w in enumerate(list(words))}
word2index['-PAD-'] = 0  # The special value used for padding
word2index['-OOV-'] = 1  # The special value used for OOVs
 
tag2index = {t: i + 1 for i, t in enumerate(list(tags))}
tag2index['-PAD-'] = 0  # The special value used to padding

#before keras convert to integers
train_sentences_X, test_sentences_X, train_tags_y, test_tags_y = [], [], [], []
 
for s in train_sentences:
	s_int = []
	for w in s:
		try:
			s_int.append(word2index[w.lower()])
		except KeyError:
			s_int.append(word2index['-OOV-'])
 
	train_sentences_X.append(s_int)
 
for s in test_sentences:
	s_int = []
	for w in s:
		try:
			s_int.append(word2index[w.lower()])
		except KeyError:
			s_int.append(word2index['-OOV-'])
 
	test_sentences_X.append(s_int)
 
for s in train_tags:
	train_tags_y.append([tag2index[t] for t in s])
 
for s in test_tags:
	test_tags_y.append([tag2index[t] for t in s])
 
print(train_sentences_X[0])
print(test_sentences_X[0])
print(train_tags_y[0])
print(test_tags_y[0])

#compute the max length of all the sequence #keras requires the sequences are of the same lenghth
MAX_LENGTH = len(max(train_sentences_X, key=len))
print(MAX_LENGTH)  

#use keras to pad sequences
from tensorflow import keras#.preprocessing.sequence.pad_sequences
#from keras.preprocessing.sequence import pad_sequences
train_sentences_X = keras.preprocessing.sequence.pad_sequences(train_sentences_X, maxlen=MAX_LENGTH, padding='post')
test_sentences_X = keras.preprocessing.sequence.pad_sequences(test_sentences_X, maxlen=MAX_LENGTH, padding='post')
train_tags_y = keras.preprocessing.sequence.pad_sequences(train_tags_y, maxlen=MAX_LENGTH, padding='post')
test_tags_y = keras.preprocessing.sequence.pad_sequences(test_tags_y, maxlen=MAX_LENGTH, padding='post')
 
print(train_sentences_X[0])
print(test_sentences_X[0])
print(train_tags_y[0])
print(test_tags_y[0])

#build LSTM architecture
#from keras.models import Sequential
#from keras.layers import Dense, LSTM, InputLayer, Bidirectional, TimeDistributed, Embedding, Activation
#from keras.optimizers import Adam
 
 
model = keras.models.Sequential()
model.add(keras.layers.InputLayer(input_shape=(MAX_LENGTH, )))
model.add(keras.layers.Embedding(len(word2index), 128))
model.add(keras.layers.Bidirectional(keras.layers.LSTM(256, return_sequences=True)))
model.add(keras.layers.TimeDistributed(keras.layers.Dense(len(tag2index))))
model.add(keras.layers.Activation('softmax'))
 
model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.Adam(0.001),
              metrics=['accuracy'])
 
model.summary()

#dense layer output: one-hot encoded tags
def to_categorical(sequences, categories):
	cat_sequences = []
	for s in sequences:
		cats = []
		for item in s:
			cats.append(np.zeros(categories))
			cats[-1][item] = 1.0
		cat_sequences.append(cats)
	return np.array(cat_sequences)

cat_train_tags_y = to_categorical(train_tags_y, len(tag2index))
print(cat_train_tags_y[0])

model.fit(train_sentences_X, to_categorical(train_tags_y, len(tag2index)), batch_size=128, epochs=40, validation_split=0.2)

scores = model.evaluate(test_sentences_X, to_categorical(test_tags_y, len(tag2index)))
print(scores[1]*100)
print(scores)
#print(f"{model.metrics_names[1]}: {scores[1] * 100}")   # acc: 99.09751977804825
