#!../../anaconda2/bin/python

from sklearn.preprocessing import LabelBinarizer
from itertools import chain
from sklearn.metrics import classification_report, confusion_matrix
import pickle

testTag = pickle.load(open('LSTMtestTag.p','rb'))
predTag = pickle.load(open('LSTMpredTag.p','rb'))

#print(testTag[0],predTag[0])
yPred = []
yTag = []
for i in range(len(testTag)):
	#print(testTag[i])
	#print(predTag[i][0:len(testTag[i])])
	#print('---')
	if len(testTag[i])<=len(predTag[i]):
		yPred.append(predTag[i][0:len(testTag[i])])
		yTag.append(testTag[i])
#print(testTag[0])
#print(yPred[0])

#for i in range(len(yPred)):
#	if not( len(testTag[i])==len(yPred[i])):
#		print(len(testTag[i]),len(yPred[i]))
#		print(testTag[i])
#		print(predTag[i])
#		print(yPred[i])

labels = ['','CO-USE_COMBUST_MJ_COMBUST_TOBACCO', 'DUAL-USE_COMBUST_MJ_VAPING_MJ', 'DUAL-USE_COMBUST_MJ_VAPE_NIC/TOBACCO', 'DUAL-USE_COMBUST_MJ_COMBUST_TOBACCO', 'DUAL-USE_VAPING_MJ_VAPING_NIC/TOBACCO','DUAL-USE_COMBUST_TOBACCO_VAPING_NIC/TOBACCO','DUAL-USE_VAPING_MJ_COMBUST_TOBACCO','POLY-USE_COMBUST_TOBACCO_COMBUST_MJ_VAPING_MJ','POLY-USE_COMBUST_TOBACCO_COMBUST_MJ_VAPING_NIC/TOBACCO','POLY_USE_COMBUST_TOABBCO_VAPING_MJ_VAPING_NIC/TOBACCO','POLY_USE_COMBUST_MJ_VAPING_MJ_VAPING_NIC/TOBACCO','COMBUST_MJ','COMBUST_TOBACCO','VAPING_MJ','VAPING_NIC/TOBACCO','BRAND','VAPING','SMOKING_CESSATION']

from sklearn.preprocessing import label_binarize
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import recall_score
#print(testTag[0],yPred[0])
yTagAll = []
yPredAll = []
for i in range(len(yTag)):
	yTagAll = yTagAll+yTag[i]
	yPredAll = yPredAll+yPred[i]

testTagMatrix = label_binarize(yTagAll, classes=labels)
predTagMatrix = label_binarize(yPredAll, classes=labels)

precision = dict()
recall = dict()
average_precision = dict()
for i in range(len(labels)):
	precision[i], recall[i], _ = precision_recall_curve(testTagMatrix[:, i],predTagMatrix[:, i])
	average_precision[i] = average_precision_score(testTagMatrix[:, i], predTagMatrix[:, i])


## A "micro-average": quantifying score on all classes jointly
precision["micro"], recall["micro"], _ = precision_recall_curve(testTagMatrix.ravel(), predTagMatrix.ravel())
average_precision["micro"] = average_precision_score(testTagMatrix, predTagMatrix,average="micro")
print('Average precision score, micro-averaged over all classes: {0:0.2f}'.format(average_precision["micro"]))
print('precision:',average_precision["micro"])
print('recall:',recall_score(testTagMatrix, predTagMatrix,average="micro"))
#print('precision:',precision)
#print('recall:', recall)

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
        
	tagset = set(lb.classes_)#-{''}#set(labels)-{''} #set(lb.classes_)-{''} 
	tagset = sorted(tagset)#NOT NEED SORTING FUNCTION: key=lambda tag: tag.split('-', 1)[::-1])
	class_indices = {cls: idx for idx, cls in enumerate(lb.classes_)}#enumerate(labels)}#enumerate(lb.classes_)}
   
	return classification_report(
                y_true_combined,
                y_pred_combined,
                labels = [class_indices[cls] for cls in tagset],
                target_names = tagset,
        )
concepts = ['VAPING_MJ','VAPING_NIC/TOBACCO','COMBUST_MJ','COMBUST_TOBACCO','BRAND','SMOKING_CESSATION']

#y_test_group = []
#y_pred_group = []
#for i in range(len(yTag)):
#	s_test = []
#	for t in yTag[i]:
#		if t in concepts:
#			s_test.append('Group_Concept')
#		else:
#			s_test.append(t)
#	y_test_group.append(s_test)
#
#	s_pred = []
#	for t in yPred[i]:
#		if t in concepts:
#			s_pred.append('Group_Concept')
#		else:
#			s_pred.append(t)
#	y_pred_group.append(s_pred)


print(bio_classification_report(yTag,yPred))















