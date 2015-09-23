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
	
	res = zip(data,labels)
	random.shuffle(res)
	training_words = [a[0] for a in res][:25600]
	training_labels = [a[1] for a in res][:25600]
	test_words = [a[0] for a in res][25600:]
	test_labels = [a[1] for a in res][25600:]

	clf = pickle.load(open('model.p','rb'))
	predicted = clf.predict(test_words)

	print np.mean(predicted==test_labels)