#!C:/Users/Greg/Anaconda/Python

import json
from time import time
from os import listdir
import re
import numpy as np
from random import shuffle
from pprint import pprint

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

#Bag of words function with json files and desired element to access
def bagOfWords(merge_list,des_string):

	#To Count how many lines we are reading
	line_count = 0

	#To store the list of words in each line
	lines = []

	#To store the unique words
	word_uniq = []
   
	# Look in first 100 articles
	for json in merge_list[:100]:
		body = json[des_string]	
		line_count += 1

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

	#Fill in Bag of Words Matrix 
	for l in xrange(len(lines)):
		for w in lines[l]:
			bag_matrix[l][word_uniq.index(w)] += 1

	#Print off dimensions of matrix
	print "%d * %d are the dimensions of bag of words matrix" % (len(bag_matrix), len(bag_matrix[0]))

	return np.array(bag_matrix)
		

def minhash(bag, numHashes):
	
	# Transpose the bag of words so columns are different articles
	# and rows are different words
	bag = zip(*bag)
	
	# Find how many rows there are to help with permutations
	permutation_length = len(bag)
	
	# Create output matrix
	minhash_output = declareMatrix(numHashes, len(bag[0]))
	for hashNum in xrange(numHashes):
		
		# Create row permutation array
		permutation = [i for i in range(permutation_length)]
		shuffle(permutation)
		
		# Go through each column, finding first non-zero
		for column in xrange(len(bag[0])):
			
			# Go through shuffled rows to find first nonzero
			for i in xrange(len(bag)):
				
				# Find current row in permutation
				curr_row = permutation[i]
				curr_item = bag[curr_row][column]
				# For first nonzero item, store iteration in which it was found
				if curr_item != 0:
					minhash_output[hashNum][column] = i+1
					break

	return minhash_output
				
		
######################################
start_time = time()
merged_json = merge_json(path)
data = bagOfWords( merged_json, "body" )
print data
print("------ %s seconds ------" % (time() - start_time))

time2 = time()
minhashed = ( minhash(data, 10)	)
s = [[str(e) for e in row] for row in minhashed]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print '\n'.join(table)
print("------ %s seconds ------" % (time() - time2))
