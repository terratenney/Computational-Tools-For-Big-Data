#!C:/Users/Greg/Anaconda/Python

from mrjob.job import MRJob
from mrjob.step import MRStep

class CommonFriends(MRJob):

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
	#Next, map the list of friends to the friends of the other pair
	def mapperCommon(self,person,list1):
		for friend in list1:
			yield sorted([person, friend]), list1;

	#Reduce to single output with an even count
	def reducerCommon(self, group, freq):
		yield group, self.find_mutual(freq);
	
	#Helper functio to change document from having a new friend each line,
	#to a list of friends
	def format_friends(self, people):
		friends_list = []
		for p in people:
			friends_list.append(p)
		return friends_list;

	def find_mutual(self, lists):
		set_first = lists.next()
		set_second = lists.next()
		return list( set(set_first).intersection(set(set_second)) );

	def steps(self):
		return [
            MRStep(mapper=self.mapperFormat,
                	reducer=self.reducerFormat),
            MRStep(mapper=self.mapperCommon,
            		reducer=self.reducerCommon)
	    ];


if __name__ == '__main__':
	CommonFriends.run()