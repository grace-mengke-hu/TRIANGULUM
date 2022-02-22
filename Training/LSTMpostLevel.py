#!../../anaconda2/bin/python

import pickle
import time
import spacy
from gensim.models.doc2vec import Doc2Vec
from gensim.models import Word2Vec
import liwc
from collections import Counter
import numpy as np
from sklearn import preprocessing

#load spacy english model
nlp = spacy.load("en_core_web_sm")
#load doc2vec
doc2vecModel = Doc2Vec.load('/uufs/chpc.utah.edu/common/home/u6022257/scripts/AnnotWFeature/enwiki_dbow/doc2vec.bin')
#LIWC
parse, category_names = liwc.load_token_parser('../LIWC/LIWC2007_English100131.dic')
#label binarizer
lb = preprocessing.LabelBinarizer()

data = pickle.load(open("postLevelPerUserDic.p",'rb'))
sortData = {}
for user in data.keys():
	sortUserList = sorted(data[user], key=lambda i:i['time'])
	sortData[user] = sortUserList

#generate feature vector and label
labelList = []
for user in sortData:
	for dic in sortData[user]:
		#get doc vector
		doc  = nlp(dic['corpus'].decode('UTF8'))
		docWordList = []
		for w in doc:
			docWordList.append(w.text)
		docVector = doc2vecModel.infer_vector(docWordList)
		dic['doc2vec'] = docVector
		
		#get LIWC vector
		counts = Counter(category for token in docWordList for category in parse(token))		
		LIWClist = counts.values()
		LIWCvector = np.array(LIWClist)
		dic['LIWC'] = LIWCvector	
		
		##stack feature vector
		#np.hstack((a,b))
		
		#get labels
		labelList.append(dic['genLabel'])

#get label with binarizer
print(labelList[1:5])
lb.fit(np.array(labelList)) #(np.array([[0, 1, 1], [1, 0, 0]]))
labels = lb.classes_

#split train and test
X_train = []
y_train = []
X_test = []
y_test = []
lengthPadding = 0
for user in sortData.keys()[0:90]:
	tmpVec = []
	tmpLabel = []
	for dic in sortData[user]:
		tmpVec.append(np.hstack((dic['doc2vec'],dic['LIWC']) ) )	
		tmpLabel.append(lb.inverse_transform(np.array( [dic['genLabel']] )))
		lengthPadding = len(dic['doc2vec'])+len(dic['LIWC'])
	X_train.append(tmpVec)#list of list of variant length
	y_train.append(tmpLabel)

for user in sortData.keys()[90:130]:
	tmpVec = []
	tmpLabel = []
	for dic in sortData[user]:
		tmpVec.append(np.hstack((dic['doc2vec'],dic['LIWC']) ))
		tmpLabel.append(lb.inverse_transform(np.array( [dic['genLabel']] )) )
	X_test.append(tmpVec)
	y_test.append(tmpLabel)

#compute the max length of all the sequence #keras requires the sequences are of the same lenghth
numPostPerUserList = []
for user in sortData.keys():
	numPostPerUserList.append(len(sortData[user]))
MAX_LENGTH = max(numPostPerUserList)
print(MAX_LENGTH)

#PADDING
paddingVec = np.zeros(lengthPadding)

def padding(listOfList, MAX_LENGTH, paddingVec ):
	outListofList = []
	for x in listOfList:
		numPad = 0
		if len(x)<MAX_LENGTH:
			numPad = MAX_LENGTH-len(x)
			for i in range(numPad):
				x.append(paddingVec)
			outListofList.append(x)
		else:
			outListofList.append(x)
	return outListofList
		
X_train_pad = padding(X_train, MAX_LENGTH, paddingVec)
y_train_pad = padding(y_train, MAX_LENGTH, np.array([[0,0,0,0,0,0]]))
X_test_pad = padding(X_test, MAX_LENGTH, paddingVec)
y_test_pad = padding(y_test, MAX_LENGTH, np.array([[0,0,0,0,0,0]]))
	

##use keras to pad sequences
from tensorflow import keras#.preprocessing.sequence.pad_sequences
##from keras.preprocessing.sequence import pad_sequences
#train_X = keras.preprocessing.sequence.pad_sequences(X_train, maxlen=MAX_LENGTH, padding='post',value = 0.0)
#test_X = keras.preprocessing.sequence.pad_sequences(X_test, maxlen=MAX_LENGTH, padding='post',value = 0.0)
#tags_y = keras.preprocessing.sequence.pad_sequences(y_train, maxlen=MAX_LENGTH, padding='post',value = 0.0)
#tags_y = keras.preprocessing.sequence.pad_sequences(y_test, maxlen=MAX_LENGTH, padding='post',value = 0.0)

#print(train_X[0])
#print(test_X[0])
#print(y_train[0])
#print(y_test[0])


model = keras.models.Sequential()
model.add(keras.layers.InputLayer(input_shape=(MAX_LENGTH, )))
model.add(keras.layers.Embedding(500, 128))
model.add(keras.layers.Bidirectional(keras.layers.LSTM(256, return_sequences=True)))
model.add(keras.layers.TimeDistributed(keras.layers.Dense(len(labels))))
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

cat_train_tags_y = to_categorical(y_train_pad, len(labels))
print(cat_train_tags_y[0])

model.fit(X_train_pad, to_categorical(y_train_pad, len(labels)), batch_size=128, epochs=40, validation_split=0.2)

scores = model.evaluate(X_test_pad, to_categorical(y_test_pad, len(labels)))
print(scores[1]*100)
print(scores)
#print(f"{mode
