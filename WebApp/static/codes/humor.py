#!/usr/bin/env python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
import numpy as np
import random
import pickle
import sys


if __name__=="__main__":
	with open('/var/www/html/nlp/Theme/data/answer.txt','w') as f:
		f.write("Very very bad")
	text = []
	with open('/var/www/html/nlp/Theme/data/answer.txt','r') as f:
		for lines in f.readlines():
			lines=lines.strip()
			text.append(lines)

	with open('/var/www/html/nlp/Theme/data/answer.txt','w') as f:
		f.write("changed")

	clf = pickle.load(open('/var/www/html/nlp/Theme/codes/model.p','rb'))
	predicted = clf.predict(text)
	


	if predicted[0]==0:
		print "Non-humourous"
	else:
		print "Humourous"