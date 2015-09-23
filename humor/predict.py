from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
import numpy as np
import random
import pickle

if __name__=="__main__":
	text = []
	with open('answer.txt','r') as f:
		for lines in f.readlines():
			lines=lines.strip()
			text.append(lines)

	clf = pickle.load(open('model.p','rb'))
	predicted = clf.predict(text)
	
	if predicted[0]==0:
		print "Non-humourous"
	else:
		print "Humourous"
	
	"""
	for i in range(len(predicted)):
		if predicted[i]==0:
			print "Non-humourous"
		else:
			print "Humourous"
	"""