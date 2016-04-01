# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
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

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/index')
def form():
	# print "hello"
	return render_template('index.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/humor', methods=['POST'])
def humor():
	
	
	answer=request.form['msg']
	answer = answer.strip()
	humor = 5;
	satire = 15;
	abusive = 20;
	formalness = 30;
	descriptive = 80;
	readability = 100;
	print answer

	################################################################################ Humor

	input1 = answer
	import humor_code
	humor = humor_code.getValue(input1)
	print "humor", humor

	################################################################################ Formalness
# 	import base64
# 	import requests
# 	from xml.dom import minidom


# 	input2 = answer
# 	# Converting code to base64
# 	s = base64.b64encode(bytes(input2))
# 	# creating xml content for query posting
# 	xml = """<?xml version="1.0" encoding="utf-8" ?>
# <uclassify xmlns="http://api.uclassify.com/1/RequestSchema" version="1.01">
#   <texts>
#     <textBase64 id="text_1">"""+s+"""</textBase64>
#   </texts>
#   <readCalls readApiKey="HoGp2i9XYbPy">
#     <classify id="call_1" username="prfekt" classifierName="Tonality" textId="text_1"/>
#   </readCalls>
# </uclassify>"""
# 	# header for http request
# 	headers = {'Content-Type':'text/xml', 'charset':'utf-8'}
# 	# posting the request
# 	r = requests.post("http://api.uclassify.com/", data = xml, headers = headers).text
# 	# parsing the response present in xml format in variable r
# 	xmldoc = minidom.parseString(r)
# 	itemlist = xmldoc.getElementsByTagName('class')
# 	num = 0.0
# 	deno = 0.0
# 	for s in itemlist:
# 		# print(s.attributes['className'].value + '\t' + s.attributes['p'].value)
# 		deno += float(s.attributes['p'].value)
# 		if s.attributes['className'].value == 'Corporate':
# 			num = float(s.attributes['p'].value)

# 	formalness = int(100*num/deno)
# 	print "formalness", formalness

	###################################################################################### Abusive

	input3 = answer
	import inappropiate
	abusive = inappropiate.getValue(input3)
	print "abusive", abusive

	###################################################################################### Readability
	import subprocess

	input4 = answer
	with open('./query.txt',"w+") as f:
		f.write(input4)

	proc = subprocess.Popen("php test.php", shell=True, stdout=subprocess.PIPE)
	script_response = proc.stdout.read()

	# print script_response

	with open('./readability.txt',"r") as f:
		output = f.readlines()

	# print output[0]

	readability = output[0]
	print "readability", readability

	###################################################################################### Descriptive

	input5 = answer
	import detail
	descriptive = detail.getValue(input5)
	print"Done"



	#############################################################################################################################################################
	message = repr(answer)
	# print message
	return render_template('result.html',humor = humor, satire = satire, abusive = abusive, formalness = formalness, descriptive = descriptive, readability = readability , message = answer)

# Run the app :)
if __name__ == '__main__':
  app.run(host="0.0.0.0",
        port=int("5000"),debug=True)
