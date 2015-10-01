#!/usr/bin/python

import string, re
from string import digits

#Function
def bagOfWords( file ):
   openFile = open(file, "r")
   read_it = openFile.read()

   #To Count how many lines we are reading
   line_count = 0

   #To store the list of words in each line
   lines = []

   #To store the unique words
   word_uniq = []
   
   for line in read_it.splitlines():
      #If line has desired string
      if line.find('"request_text":') > -1:
	 #increment line count		
	 line_count += 1
	
	 #Collect string, make lowercase, remove digits, remove
	 #punctuation, remove email addresses, remove websites
	 #and split into words for easier access		
	 text = line.partition(': ')[2]
	 text = text.lower()
	 text = re.sub('[\[\]!~*\-,><}{;)(:#$"&%.?]',' ',text)
	 text = text.replace("\\n",' ')
	 text = re.sub('[\\/]',' ',text)
	 text = ' '.join([i for i in text.split() if not i.isdigit() and not "@" in i and not "http" in i])

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
   for l in lines:
	for w in l:
		bag_matrix[lines.index(l)][word_uniq.index(w)] += 1

   #Print off dimensions of matrix
   print "%d * %d are the dimensions of bag of words matrix" % (len(bag_matrix), len(bag_matrix[0]))
		
   openFile.close();   

#Function for creating 2D matrix of size x*y
def declareMatrix(x,y):
	matrix = [[0]*y for i in range(x)]
	return matrix;
 
#Function Call
bagOfWords("pizza-train.json")
