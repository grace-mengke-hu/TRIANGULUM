#!../../anaconda2/bin/python

def multiClass_precicion_recall(classLabelList, vectorTestLabel, vectorPred):
	from sklearn.preprocessing import label_binarize
	testLabel_sampleXclass = label_binarize(vectorTestLabel,classes=classLabelList)
	predLabel_sampleXclass = label_binarize(vectorPred, classes=classLabelList)

	from sklearn.metrics import precision_recall_curve
	from sklearn.metrics import average_precision_score
	# For each class
	precision = dict()
	recall = dict()
	average_precision = dict()

	for i in range(len(classLabelList)):
		precision[i], recall[i], _ = precision_recall_curve(testLabel_sampleXclass[:, i], predLabel_sampleXclass[:, i])
		average_precision[i] = average_precision_score(testLabel_sampleXclass[:, i], predLabel_sampleXclass[:, i])

	precision["micro"], recall["micro"], _ = precision_recall_curve(testLabel_sampleXclass.ravel(),predLabel_sampleXclass.ravel())
	average_precision["micro"] = average_precision_score(testLabel_sampleXclass, predLabel_sampleXclass, average="micro")

	return precision, recall, average_precision
		
