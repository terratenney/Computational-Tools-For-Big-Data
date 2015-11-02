#!C:/Users/Greg/Anaconda/Python

from mrjob.job import MRJob
from mrjob.step import MRStep

class Triangles(MRJob):

	#First Round -----------------------
	#First split each line into different nodes and then count how many times they appear
	def mapperFormat(self, _, line):
		people = line.split()
		yield int(people[0]), int(people[1])
		yield int(people[1]), int(people[0]);

	#Then we reduce this list of nodes into
	#number of edges it has
	def reducerFormat(self, key, values):
		yield key, self.format_friends(values);

	#Second Round ----------------------
	#Next, map the list of items to the items of the other pair
	def mapperCommon(self,person,list1):
		for friend in list1:
			yield sorted([person, friend]), list1;

	#Reduce to single output with an even count
	def reducerCommon(self, group, freq):
		yield group, self.find_mutual(freq);

	#Gets the number of mutual friends per group
	def reducerMutual(self, group, mutual):
		yield None, sum(self.count(mutual));

	# Finds total number of mutual items, and divides by 3 to get triangles.
	#Since it is represented 3 times
	def reducerTriangle(self, _, mutual_group):
		yield "Number of triangles: ", sum(mutual_group)/3;
	
	#Helper functio to change document from having a new friend each line,
	#to a list of friends
	def format_friends(self, people):
		friends_list = []
		for p in people:
			friends_list.append(p)
		return friends_list;

	#Intersects to find mutual friends
	def find_mutual(self, lists):
		set_first = lists.next()
		set_second = lists.next()
		return list( set(set_first).intersection(set(set_second)) );

	#Counts the number of items given
	def count(self, items):
		for i in items:
			yield len(i);

	def steps(self):
		return [
            MRStep(mapper=self.mapperFormat,
                	reducer=self.reducerFormat),
            MRStep(mapper=self.mapperCommon,
            		reducer=self.reducerCommon),
            MRStep(reducer=self.reducerMutual),
			MRStep(reducer=self.reducerTriangle)
	    ];


if __name__ == '__main__':
	Triangles.run()