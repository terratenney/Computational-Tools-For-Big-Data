#!C:/Users/Greg/Anaconda/Python

import json
from time import time
from os import listdir
import re
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import mmh3


#Folder with json files
path = "./json/"
# Function to load all json files into python
def merge_json(path):
	merged_json = []
	for filename in listdir(path):
		with open(path + filename) as json_file:
			json_data = json.load(json_file)
			
			# Filter out any articles that don't contain topics or body
			json_data = filter(lambda x: "topics" in x.keys() and "body" in x.keys(), json_data)
			merged_json += json_data
	return merged_json

#Function for creating 2D matrix of size x*y
def declareMatrix(x,y):
	matrix = [[0]*y for i in range(x)]
	return matrix;

#Random Forest Classifier Function
def randomforest(data):
	xData = data[0]
	yData = data[1]

	yData_Vec = []

	#Transform Y Data into a Vector
	for i in yData:
		if i[0] == 1:
			yData_Vec.append(0)
		else:
			yData_Vec.append(1)
			
	#Set 80% Training Data and 20% Test Data
	xtotal_training_samples = round(xData.shape[0] * 0.8)
	ytotal_training_samples = int( round(0.8 * len(yData_Vec)) )
	xtotal_test_samples = round(xData.shape[0] * 0.2)
	ytotal_test_samples = int( round(0.2 * len(yData_Vec)) )

	xTrain = np.array( xData[:xtotal_training_samples] )
	yTrain = np.array( yData_Vec[:ytotal_training_samples] )

	xTest = np.array( xData[-xtotal_test_samples:] )
	yTest = np.array( yData_Vec[-ytotal_test_samples:] )

	#Build model with 50 trees
	forestModel = RandomForestClassifier(50)

	#Train it
	forestModel.fit(xTrain, yTrain)

	#Check accuracy of prediciton
	print ("The Classifier Predicts With %f Percent Accuracy" % (forestModel.score(xTest, yTest)*100) )

#################################################################
#Bag of words function with json files and desired element to access
def bagOfWords(merge_list):

	#To Count how many lines we are reading
	line_count = 0

	#To store the list of words in each line
	lines = []

	#Whether earn is in topics or not
	output = []

	#To store the unique words
	word_uniq = []
   
	for json in merge_list:
		#for body in json:
		body = json["body"]	
		line_count += 1

		#Check the output
		if "earn" in json["topics"]:
			output.append(1)
		else:
			output.append(0)

		#Collect string, make lowercase, remove digits, remove
		#punctuation, remove email addresses, remove websites
		#and split into words for easier access		
		text = body.lower()
		text = re.sub('[\[\]!~*\-,><}{;)(:#$"&%.?]',' ',text)
		text = text.replace("\\n",' ')

		text = text.split()
 
		for word in text:
			if word in word_uniq:		#If word is in list of unique words, do nothing
				next
			else:
				word_uniq.append(word)  #Add to unique word list

		#Add the line's words to a line list
		lines.append(text)

	#Declare Bag of Words Matrix
	bag_matrix = declareMatrix(line_count,len(word_uniq))
	bag_matrix_out = declareMatrix(line_count,2)

	#Fill in Bag of Words Matrix 
	for l in xrange(len(lines)):

		#Fill words
		for w in lines[l]:
			bag_matrix[l][word_uniq.index(w)] += 1

		#Fill output
		if output[l] == 1:
			bag_matrix_out[l][1] = 1
		else:
			bag_matrix_out[l][0] = 1

	#Print off dimensions of matrix
	print "%d * %d are the dimensions of bag of words matrix" % (len(bag_matrix), len(bag_matrix[0]))

	print "%d * %d are the dimensions of output matrix" % (len(bag_matrix_out), len(bag_matrix_out[0]))

	result = []
	result.append(np.array(bag_matrix))
	result.append(np.array(bag_matrix_out))
	return result
		
#################################################################
#Feature Hashing Function
def featurehash(merge_list,buckets):
	#To Count how many lines we are reading
	line_count = 0

	#To store the list of words in each line
	lines = []

	#Whether earn is in topics or not
	output = []

	#To store the unique words
	word_uniq = []
   
	for json in merge_list:
		body = json["body"]	
		line_count += 1

		#Check the output
		if "earn" in json["topics"]:
			output.append(1)
		else:
			output.append(0)

		#Collect string, make lowercase, remove digits, remove
		#punctuation, remove email addresses, remove websites
		#and split into words for easier access		
		text = body.lower()
		text = re.sub('[\[\]!~*\-,><}{;)(:#$"&%.?]',' ',text)
		text = text.replace("\\n",' ')

		text = text.split()

		indices = []

		for word in text:
			idx = mmh3.hash(word.encode('utf-8')) % buckets
			indices.append(idx)

		#Add the line's words to a line list
		lines.append(indices)

	#Declare Hashtables
	hashtable = declareMatrix(line_count,buckets)
	hashtable_out = declareMatrix(line_count,2)

	#Fill in Bag of Words Matrix 
	for l in xrange(len(lines)):

		#Fill words
		for i in lines[l]:
			hashtable[l][i] += 1 	#Fill in every index hashed

		#Fill output
		if output[l] == 1:
			hashtable_out[l][1] = 1
		else:
			hashtable_out[l][0] = 1

	#Print off dimensions of matrix
	print "%d * %d are the dimensions of bag of words matrix" % (len(hashtable), len(hashtable[0]))

	print "%d * %d are the dimensions of output matrix" % (len(hashtable_out), len(hashtable_out[0]))

	result = []
	result.append(np.array(hashtable))
	result.append(np.array(hashtable_out))
	return result

##############################################
#Bag of words method
start_time = time()
randomforest(bagOfWords( merge_json(path) ))
print("------ %s seconds ------" % (time() - start_time))

#Feature hash method
start_time = time()
randomforest(featurehash( merge_json(path),1000 ))
print("------ %s seconds ------" % (time() - start_time))