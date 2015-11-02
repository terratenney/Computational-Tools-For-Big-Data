#!C:/Users/Greg/Anaconda/Python

from mrjob.job import MRJob
from string import punctuation,maketrans

class MRWordFrequencyCount(MRJob):

	def mapper(self, _, line):
		#Convert line to lowercase and remove punctuation
		table = maketrans("","")
		words = line.translate(table, punctuation)
		words = words.lower()
		#Take each word and give it a value of 1
		words = words.split()
		for w in words:
			yield w, 1;

	def reducer(self, key, values):
		#Sum word values
		yield key, sum(values);


if __name__ == '__main__':
	MRWordFrequencyCount.run()