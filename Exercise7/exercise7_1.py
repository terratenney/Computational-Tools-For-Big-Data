#!C:/Users/Greg/Anaconda/Python

import mmh3
from math import log,ceil
from bitarray import bitarray
from string import punctuation,maketrans
from time import time

#Bloom Filter class
class Bloom:
	#Constructor
	def __init__(self, bitsize, runs):
		self.bitsize = bitsize
		self.runs = runs
		self.array = bitarray(bitsize)
		self.array.setall(0)

	#Add method
	def add(self,string):
		for seed in xrange(self.runs):
			result = mmh3.hash(string, seed) % self.bitsize
			self.array[result] = 1;

	#Lookup method
	def lookup(self,string):
		for seed in xrange(self.runs):
			result = mmh3.hash(string, seed) % self.bitsize
			if self.array[result] == 0:
				return False
		return True;

#Function to determine number of hash functions
def num_Hashfunc(size, n):
	return size / n * log(2);

#Check Actual amount of words in dictionary
def check(dict, words):
	real_count  = 0
	for w in words:
		if w in dict:
			real_count += 1

	return real_count;


#Execution of faster method
def main():
	start_time = time()

	openFile = open("dict", "r")
	read_it = openFile.read()

	#Calculate number of words in dictionary for n
	words = 0
	for line in read_it.splitlines():
		words += 1

	#Calculate number of hash functions
	num_hash = ceil( num_Hashfunc(1000000,words) )

	#Construct new filter
	filter = Bloom(1000000,int(num_hash))

	#Add and hash dictionary
	dictionary = []
	for line in read_it.splitlines():
		filter.add(line)
		dictionary.append(line)

	#Lookup Shakespeare
	shakeFile = open("shakespeare.txt", "r")
	shake_read = shakeFile.read()

	count = 0
	word_array = []
	#Remove Punctuation and Lower case
	for line in shake_read.splitlines():
		table = maketrans("","")
		text = line.translate(table, punctuation)
		text = text.lower()
		text = text.split()

		#If it is valid and not already in the array, add it and count it
		for word in text:
			if filter.lookup(word) == True and word not in word_array:
				word_array.append(word)
				count += 1

	#Calculated words in dictionary
	print "%d shakespeare words in dict" % count
	#Run time
	print("--- %s seconds ---" % (time() - start_time))
	#Actual words in dictionary
	print "%d actual amount in dict \n" % check(dictionary, word_array)

	openFile.close()
	shakeFile.close();

#Execution of slow method
def main_slow():
	start_time = time()

	openFile = open("dict", "r")
	read_it = openFile.read()

	#Add words from dictionary to an array
	dictionary = []
	for line in read_it.splitlines():
		dictionary.append(line)

	#Lookup Shakespeare
	shakeFile = open("shakespeare.txt", "r")
	shake_read = shakeFile.read()

	count = 0
	word_array = []
	#Remove Punctuation and Lower case
	for line in shake_read.splitlines():
		table = maketrans("","")
		text = line.translate(table, punctuation)
		text = text.lower()
		text = text.split()

		#If it is valid and not already in the array, add it and count it
		for word in text:
			if word in dictionary and word not in word_array:
				word_array.append(word)
				count += 1

	#Calculated words in dictionary
	print "%d shakespeare words in dict" % count
	#Run time
	print("--- %s seconds ---" % (time() - start_time))
	#Actual words in dictionary
	print "%d actual amount in dict \n" % check(dictionary, word_array)
	
	openFile.close()
	shakeFile.close();

print "Hash Method"
main()
print "Slow Method"
main_slow()