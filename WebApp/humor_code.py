import pickle

def getValue(answer):


	clf = pickle.load(open('model_regression.p','rb'))
	predicted = clf.predict(answer)

	predicted[0]=max(0,min(predicted[0],1))
	return predicted[0]*100.0