#!../../anaconda2/bin/python

import pickle
import CRFpostLevelFeature

from itertools import chain
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report, confusion_matrix
import pycrfsuite
import time


data = pickle.load(open("postLevelPerUserDic.p",'rb'))

print(len(data.keys()))

#print(data['Obvious'])
#sort time
sortData = {}
for user in data.keys():
	sortUserList = sorted(data[user], key=lambda i:i['time'])
	sortData[user] = sortUserList

#split train and test
X_train = []
y_train = []
X_test = []
y_test = []
for user in sortData.keys()[0:90]:
	#each user is one data point
	X_train.append(CRFpostLevelFeature.userList2features(sortData[user]))
	y_train.append(CRFpostLevelFeature.userList2labels(sortData[user]))
for user in sortData.keys()[90:130]:
	X_test.append(CRFpostLevelFeature.userList2features(sortData[user]))
        y_test.append(CRFpostLevelFeature.userList2labels(sortData[user]))

#create pycrfsuite.Trainer and load the training data to CRFsuite
time_start = time.time()
trainer = pycrfsuite.Trainer(verbose=False)

for xseq, yseq in zip(X_train, y_train):
	trainer.append(xseq, yseq)

#Set training parameters. We will use L-BFGS training algorithm (it is default) with Elastic Net (L1 + L2) regularization.
trainer.set_params({
    'c1': 1.0,   # coefficient for L1 penalty
    'c2': 1e-3,  # coefficient for L2 penalty
    'max_iterations': 50,  # stop earlier

    # include transitions that are possible, but not observed
    'feature.possible_transitions': True
})

print(trainer.params())
time_train_end = time.time()
print("TRAINING TIME:", time_train_end-time_start)

#Training
#%%time
trainer.train('postLevel.crfsuite')
print(trainer.logparser.last_iteration)



##Testing
tagger = pycrfsuite.Tagger()
tagger.open('postLevel.crfsuite')
y_pred = [tagger.tag(xseq) for xseq in X_test]
time_test_end = time.time()
print("TESTING TAGGING:",time_test_end-time_start)



#evaluation function
def bio_classification_report(y_true, y_pred):
        """
        Classification report for a list of BIO-encoded sequences.
        It computes token-level metrics and discards "O" labels.
    
        Note that it requires scikit-learn 0.15+ (or a version from github master)
        to calculate averages properly!
        """
	lb = LabelBinarizer()
	y_true_combined = lb.fit_transform(list(chain.from_iterable(y_true)))
	y_pred_combined = lb.transform(list(chain.from_iterable(y_pred)))

	tagset = set(lb.classes_)-{''}
	tagset = sorted(tagset)#NOT NEED SORTING FUNCTION: key=lambda tag: tag.split('-', 1)[::-1])
	class_indices = {cls: idx for idx, cls in enumerate(lb.classes_)}

	return classification_report(
                y_true_combined,
                y_pred_combined,
                labels = [class_indices[cls] for cls in tagset],
                target_names = tagset,
        )

#Evaluation
print(bio_classification_report(y_test, y_pred))

