#!../../anaconda2/bin/python

import pickle
import numpy as np
from sklearn.model_selection import train_test_split

DataVecList = pickle.load( open( "relationDataVectorList.p", "rb" ) )
labelList = pickle.load(open( "relationDataLabelList.p", "rb" ))
catList = pickle.load(open("relationAllCategoryList.p","rb"))

cat = np.array(catList)

# dividing X, y into train and test data 
X_train, X_test, y_train, y_test = train_test_split(DataVecList, labelList, test_size=0.33, random_state=42)

from sklearn.metrics import average_precision_score

# training a linear SVM classifier 
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix 
#svm model
svmClassifier = SVC(kernel = 'linear', C = 1)
#svm training
svmLinearModel = svmClassifier.fit(X_train, y_train) 
#svm predictions
svm_predictions = svmLinearModel.predict(X_test) 
#svm evaluation
accuracy = svmLinearModel.score(X_test, y_test) 
# creating a confusion matrix 
cm = confusion_matrix(y_test, svm_predictions,catList) 

#multi layer classification
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(50,100, 50), random_state=3)
MLPmodel = clf.fit(X_train,y_train)
MLP_predictions = MLPmodel.predict(X_test)
accuracy_MLP = MLPmodel.score(X_test,y_test)

#KNN
# training a KNN classifier 
from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors = 37).fit(X_train, y_train)
knn_predictions = knn.predict(X_test) 
accuracy_KNN = knn.score(X_test, y_test)  

# training a Naive Bayes classifier 
from sklearn.naive_bayes import GaussianNB 
gnb = GaussianNB().fit(X_train, y_train) 
gnb_predictions = gnb.predict(X_test) 
accuracy_NB = gnb.score(X_test, y_test) 

#random forest
from sklearn.ensemble import RandomForestClassifier
randForest = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 42)
randForest.fit(X_train, y_train)
randForest_predictions = randForest.predict(X_test)
accuracy_randForest = randForest.score(X_test,y_test)

print('svm accuracy:',accuracy,'MLP accuracy:',accuracy_MLP, 'KNN accuracy:',accuracy_KNN, 'Naive Bayes accuracy', accuracy_NB,'random forest:',accuracy_randForest)

#print(cm.shape)
#print(len(catList))


#from sklearn.preprocessing import label_binarize
origCat = catList
catList.remove(' ')
#nClass= catList.remove(' ')
import precision_recall
precisionSVM,recallSVM,averagePrecisionSVM = precision_recall.multiClass_precicion_recall(catList, y_test, svm_predictions)
precisionMLP,recallMLP,averagePrecisionMLP = precision_recall.multiClass_precicion_recall(catList, y_test, MLP_predictions)
precisionKNN, recallKNN, averagePrecisionKNN = precision_recall.multiClass_precicion_recall(catList, y_test, knn_predictions)
precisionNB, recallNB, averagePrecisionNB = precision_recall.multiClass_precicion_recall(catList, y_test, gnb_predictions)
precisionRF,recallRF,averagePrecisionRF = precision_recall.multiClass_precicion_recall(catList, y_test, randForest_predictions)

print('Average precision SVM:',averagePrecisionSVM["micro"],'MLP:',averagePrecisionMLP["micro"],'KNN',averagePrecisionKNN["micro"],"NB:",averagePrecisionNB["micro"],"RF:",averagePrecisionRF["micro"])
#svn_pred_sampleXclassArray = label_binarize(svm_predictions, classes=catList)
#y_test_sampleXclassArray = label_binarize(y_test, classes = catList)

#from sklearn.metrics import precision_recall_curve
#from sklearn.metrics import average_precision_score
# For each class
#precision = dict()
#recall = dict()
#average_precision = dict()
#for i in range(len(catList)):
#	precision[i], recall[i], _ = precision_recall_curve(y_test_sampleXclassArray[:, i], svn_pred_sampleXclassArray[:, i])
#	average_precision[i] = average_precision_score(y_test_sampleXclassArray[:, i], svn_pred_sampleXclassArray[:, i])

## A "micro-average": quantifying score on all classes jointly
#precision["micro"], recall["micro"], _ = precision_recall_curve(y_test_sampleXclassArray.ravel(),svn_pred_sampleXclassArray.ravel())
#average_precision["micro"] = average_precision_score(y_test_sampleXclassArray, svn_pred_sampleXclassArray, average="micro")
#print('Average precision score, micro-averaged over all classes: {0:0.2f}'.format(average_precision["micro"]))
#print(precision)
#print(recall)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(recallSVM['micro'], precisionSVM['micro'],color = 'red',label = 'SVM')
plt.plot(recallMLP['micro'], precisionMLP['micro'],color='olive',label = 'MLP')
plt.plot(recallKNN['micro'], precisionKNN['micro'],color='blue',label = 'KNN')
plt.plot(recallNB['micro'], precisionNB['micro'],color='black',label = 'Naive Bayes')
plt.plot(recallRF['micro'], precisionRF['micro'],color='brown',label = 'Random Forest')
#plt.step(recall['micro'], precision['micro'], where='post')
plt.legend(loc="upper right")
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
print('Average precision SVM:',averagePrecisionSVM["micro"],'MLP:',averagePrecisionMLP["micro"],'KNN',averagePrecisionKNN["micro"],"NB:",averagePrecisionNB["micro"],"RF:",averagePrecisionRF["micro"])
#plt.title('Average precision score, micro-averaged over all classes:1) SVM AP={0:0.2f};'.format(averagePrecisionSVM["micro"])+'2) MLP AP = {0:0.2f}'.format(averagePrecisionMLP["micro"]))
#plt.title('Average precision MLP score, micro-averaged over all classes: AP={0:0.2f}'.format(averagePrecisionMLP["micro"]))
#plt.show()	

#print(svn_pred_sampleXclassArray)
#print(y_test)
#average precision recall in multi class setting
#from sklearn.metrics import precision_recall_curve
#from sklearn.metrics import average_precision_score
## For each class
#precision = dict()
#recall = dict()
#average_precision = dict()

#for i in range(len(catList)):#number of classes
#    precision[i], recall[i], _ = precision_recall_curve(y_test[:, i], svm_predictions[:, i])
#    average_precision[i] = average_precision_score(y_test[:, i], svm_predictions[:, i])

## A "micro-average": quantifying score on all classes jointly
#precision["micro"], recall["micro"], _ = precision_recall_curve(y_test.ravel(),svm_predictions.ravel())
#average_precision["micro"] = average_precision_score(y_test, svm_predictions, average="micro")
#print('Average precision score, micro-averaged over all classes: {0:0.2f}'.format(average_precision["micro"]))
