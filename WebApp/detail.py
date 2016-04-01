from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
import numpy as np
import random
import pickle
from os import walk
import os
import re

import xml.etree.ElementTree as ET
import glob, pickle, sys, json

import math, string, nltk
from nltk.tag import pos_tag
from collections import Counter
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.tokenize import word_tokenize

def getFeatures( Orig_Answer ):

    #Raw length in Answer (A_Raw_Length) in words.
    Answer = Orig_Answer.lower()
    Answer_WO_Punc = Answer.translate(None, string.punctuation)     #removing all the punctation from the answer
    list_AWOP = Answer_WO_Punc.split()

    A_Raw_Length = len(list_AWOP)
    A_Sentence_Length = len(Answer.split('.'))

    A_tokens = nltk.word_tokenize(Orig_Answer)
    A_pos_tagged = pos_tag(A_tokens)

    #Counting Entropy of words
    A_Entropy = 0
    word_counts,word_prob = defaultdict(int), defaultdict(float)
    
    word_counts = Counter(word for word in list_AWOP) #Count of each word appearing how many times

    for w, c in word_counts.iteritems():
        prob = float(c)/A_Raw_Length    #Probability of each word appearing
        A_Entropy -= prob*math.log10(prob)

    #Counting Punctuator density
    Count_punc = sum(Counter(tag for tag in A_tokens if tag in string.punctuation).values())
    if(A_Raw_Length==0):
        A_Punct_Density = 0
    else:
        A_Punct_Density = float(Count_punc)/A_Raw_Length

    #finding proper noun count
    A_pos_counts = Counter(tag for word,tag in A_pos_tagged)
    A_pos = set(tag for word,tag in A_pos_tagged)
    A_Nouns = A_pos_counts["NNP"] + A_pos_counts["NN"] + A_pos_counts["NNPS"] +  A_pos_counts["NNS"]

    #finding verb count
    A_Verb = A_pos_counts["VBP"] + A_pos_counts["VB"] + A_pos_counts["VBD"] + A_pos_counts["VBG"] + A_pos_counts["VBN"]  + A_pos_counts["VBZ"]

    #finding no. of stop words
    stopword_list = stopwords.words('english')
    nonstopwords = [word for word in Answer if word not in stopword_list ]
    A_NonStopwords = len(nonstopwords)

    A_Links = Answer.count("http")

    '''
    print "Answer length",A_Raw_Length,"words"
    print "Entropy of Answer",A_Entropy
    print "Punctuator density",A_Punct_Density
    print "Total Count of Nouns used",A_Nouns
    print "Total Count of Verb used",A_Verb
    print "Number of Non-stop words",A_NonStopwords
    '''

    features = [A_Raw_Length,A_Sentence_Length, A_Entropy,A_Punct_Density,A_Nouns,A_Verb,A_NonStopwords,A_Links]
    #features = [A_Raw_Length]
    
    return features


def remove_non_ascii_2(text):
    return re.sub(r'[^\x00-\x7F]','', text)


def getValue(answer):

    reload(sys)  
    sys.setdefaultencoding('utf8')

    # answer = "Adam-Carmack_Is the game of GO popular outside Asia?.txt"
    # answer = answer*10
    #answer = raw_input("Enter text\n")
    answer = answer.encode("ascii","ignore")
    feature = getFeatures(answer)
    count_images = 0
    feature.append(count_images)
    clf = pickle.load(open('model_regression_s.p','rb'))
    predicted = clf.predict([feature])
    if(predicted < 0):
        predicted = 0
    if(predicted > 1):
        predicted = 1

    return(predicted*100)