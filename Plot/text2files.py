#!../../anaconda2/bin/python
import pickle


txtList = pickle.load(open("cessation_submissionTXT_2013-2018.p","rb"))
print(txtList[0])
for i in range(len(txtList)):
	fp = open('cessation/'+str(i)+'.txt','w')
	fp.write(txtList[i].encode('utf-8'))
	fp.close()


