#!C:/Users/Greg/Anaconda/Python

import mmh3
from math import pow
from bitarray import bitarray
from string import punctuation,maketrans
from time import time
from random import sample

#Flajolet-Martin class
class Flajolet:
	#Constructor
	def __init__(self,hashes,groups):
		#Number of hashes
		self.num_hash = hashes
		#Number of groups
		self.groups = groups
		#An array of bitmaps size 32 bit int
		self.r_array = []
		for array in xrange(groups*hashes):
			self.r_array.append(32*bitarray([0]))
		#All the seeds used in the hash functions
		self.seeds = sample(xrange(1000),groups*hashes)

	#Process method
	def process(self,element):
		seed_idx = 0
		#For every group, do num_hash hashes
		for gr in xrange(self.groups):
			for s in xrange(self.num_hash):
				#Hash each string and calculate trailing zeros
				number = mmh3.hash(element, self.seeds[seed_idx]) 
				zeros = self.trailing_zeroes(int(number))

				#Fill in trailing zeros index in array
				if self.r_array[seed_idx][zeros] == 0:
					self.r_array[seed_idx][zeros] = 1

				seed_idx += 1;

	#Calculate the median value of an array
	def median_func(self,array):
		median = array
		median.sort()
		length = len(median)
		#If length even
		if length % 2 == 0:
			high = median[length/2]
			low = median[length/2-1]
			median = (high+low)/float(2)
		#If length odd
		else:
			mid = length/2
			median = median[mid]
		return median;

	#Calculate Cardinality Estimate
	def give_estimate(self,value):
		estimate = pow(2.0,value) / 0.77351
		return estimate;

	#Counts the number of trailing 0 bits in num
	#Size 32 bit int
	def trailing_zeroes(self, num):
		if num == 0:
			return 32
		p = 0
		while (num >> p) & 1 == 0:
			p += 1
		return p;

	#Find index of first zero in bitarray
	def find_zero(self,bitarray):
		idx = 0;
		while (bitarray[idx] & 1) == 1:
			idx += 1
		return idx;

#Main Function
def main():
	start_time = time()
	#Open and Read file
	openFile = open("shakespeare.txt", "r")
	read_it = openFile.read()

	#Remove Punctuation and Lower case
	table = maketrans("","")
	text = read_it.translate(table, punctuation)
	text = text.lower()

	#Set number of hash functions and groups
	hash = 10
	groups = 100
	#Construct Algorithm
	fm = Flajolet(hash,groups)
	#Mean of all medians of every group
	mean = 0

	#Actual Unique words in Shakespeare
	word_uniq = []

	for line in text.splitlines():
		words = line.split()
		#Process every word
		for word in words:
			if word not in word_uniq:
				word_uniq.append(word)
			fm.process(word)

	#Calculating Medians Per Group
	start = 0
	end = fm.num_hash
	#Find index of first zero in bit array,
	#then calculate median
	for g in xrange(fm.groups):
		temp = fm.r_array[start:end]
		med = []
		for num in temp:
			med.append(fm.find_zero(num))

		#Add to Mean variable
		mean += fm.median_func(med)

		start += fm.num_hash
		end += fm.num_hash
	#Give estimate on calculated mean
	print "Calculated Distinct Words %f" % fm.give_estimate(mean/groups)
	print "Actual Distinct Words %d" % len(word_uniq)

	print("--- %s seconds ---" % (time() - start_time));

#Execution
main()