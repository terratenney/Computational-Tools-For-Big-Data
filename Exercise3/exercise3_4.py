#!C:/Users/Greg/Anaconda/Python

import string, re
from string import digits
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
import numpy as np

#Function
def bagOfWords( file, desString ):
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
      if line.find(desString) > -1:
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
   for l in range(0,len(lines)):
	for w in lines[l]:
		bag_matrix[l][word_uniq.index(w)] += 1
		
   bag_matrix = np.array(bag_matrix)
		
   openFile.close()
   return bag_matrix;   

#Function for creating 2D matrix of size x*y
def declareMatrix(x,y):
	matrix = [[0]*y for i in range(x)]
	return matrix;
 
#Function Call

#Collect Text and Receive Pizza Data
xData = bagOfWords("pizza-train.json", '"request_text":')
yData = bagOfWords("pizza-train.json", '"requester_received_pizza":')
yData_Vec = []

#Transform Receive Pizza Data into a Vector
for i in yData:
	if i[0] == 1:
		yData_Vec.append(0)
	else:
		yData_Vec.append(1)
		
#Set 90% Training Data and 10% Test Data
xtotal_training_samples = round(xData.shape[0] * 0.9)
ytotal_training_samples = int( round(0.9 * len(yData_Vec)) )
xtotal_test_samples = round(xData.shape[0] * 0.1)
ytotal_test_samples = int( round(0.1 * len(yData_Vec)) )

xTrain = np.array( xData[:xtotal_training_samples] )
yTrain = np.array( yData_Vec[:ytotal_training_samples] )

xTest = np.array( xData[-xtotal_test_samples:] )
yTest = np.array( yData_Vec[-ytotal_test_samples:] )

#Build the Model
lrModel = linear_model.LogisticRegression()

#Train it
lrModel.fit(xTrain, yTrain)

#Check accuracy of prediciton
print ("The Classifier Predicts With %f Percent Accuracy" % (lrModel.score(xTest, yTest)*100) ) 
