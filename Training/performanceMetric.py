#import numpy as np
#PPV: positive prediction value
def precision(label, confusion_matrix):
	col = confusion_matrix[:, label]
	return confusion_matrix[label, label] / float(col.sum())
    
#sensitivity
def recall(label, confusion_matrix):
	row = confusion_matrix[label, :]
	return confusion_matrix[label, label] / float(row.sum())

#specificity: TN/(TN+FP)
def specificity(label,confusion_matrix):
	sum_of_all_elements = confusion_matrix.sum()
	row = confusion_matrix[label,:]
	col = confusion_matrix[:,label]

	true_neg_rate = (row.sum()-confusion_matrix[label, label])/float(sum_of_all_elements-col.sum())
	return 1-true_neg_rate 

#overall specificity
def specificity_macro_average(confusion_matrix):
	rows, columns = confusion_matrix.shape
	sum_of_specificity = 0
	for label in range(rows):
		sum_of_specificity += specificity(label,confusion_matrix)
	return sum_of_specificity / float(rows)

#overall PPV
def precision_macro_average(confusion_matrix):
	rows, columns = confusion_matrix.shape
	sum_of_precisions = 0
	for label in range(rows):
		sum_of_precisions += precision(label, confusion_matrix)
	return sum_of_precisions / float(rows)

#overall sensitivity
def recall_macro_average(confusion_matrix):
	rows, columns = confusion_matrix.shape
	sum_of_recalls = 0
	for label in range(columns):
		sum_of_recalls += recall(label, confusion_matrix)
	return sum_of_recalls / float(columns)

#accuracy
def accuracy(confusion_matrix):
	diagonal_sum = confusion_matrix.trace()
	sum_of_all_elements = confusion_matrix.sum()
	return diagonal_sum / float(sum_of_all_elements) 
