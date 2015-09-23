from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
import numpy as np
import random
import pickle

if __name__=="__main__":
	data = []
	labels = []
	training_words = []
	training_labels = []
	test_words = []
	test_labels = []

	with open("./dataset/jokes.txt") as f:
		for lines in f.readlines():
			lines=lines.strip()
			data.append(lines)
			labels.append(1)

	with open("./dataset/serious.txt") as f:
		for lines in f.readlines():
			lines=lines.strip()
			data.append(lines)
			labels.append(0)

	#print vectorizer.get_feature_names()
	#train = vectorizer.fit_transform(training_words)
	#print train.shape

	#Multinomial Classifier
	#clf = Pipeline([('vect',CountVectorizer()),('clf',MultinomialNB()),])

	#SVM classifier
	#clf = Pipeline([('vect',CountVectorizer()),('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42)),])
	#SVM n-gram
	clf = Pipeline([('vect',CountVectorizer(ngram_range=(1, 2),token_pattern=r'\b\w+\b', min_df=1)),('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42)),])
	
	res = zip(data,labels)
	random.shuffle(res)
	training_words = [a[0] for a in res]
	training_labels = [a[1] for a in res]
	test_words = [a[0] for a in res][25600:]
	test_labels = [a[1] for a in res][25600:]

	clf.fit(training_words,training_labels)
	pickle.dump(clf,open('model.p','wb'))
	exit()
	
	#test = vectorizer.transform(test_words)
	#predicted = clf.predict(test)
	predicted = clf.predict(test_words)

	#for actual,pred in zip(test_labels,predicted):
	#	print('%r => %s' %(actual,pred))

	print np.mean(predicted==test_labels)