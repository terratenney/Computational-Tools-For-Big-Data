#!C:/Users/Greg/Anaconda/Python

from mrjob.job import MRJob
from mrjob.step import MRStep

class Euler(MRJob):

	def mapper(self, _, line):
		nodes = line.split()
		for n in nodes:
			yield n, 1;

	def reducer(self, key, values):
		yield None, sum(values);

	def reducer_euler(self, _, edges):
		yield "Graph has an Euler Tour", self.isEven(edges);

	def steps(self):
		return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_euler)
	    ];

	def isEven(self, num):
		for node in num:
			if node % 2 != 0:
				return False
		return True;


if __name__ == '__main__':
	Euler.run()