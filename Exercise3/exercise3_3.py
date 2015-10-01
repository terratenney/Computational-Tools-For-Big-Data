#!C:/Users/Greg/Anaconda/Python
import pandas as pd
import numpy as np

#Creat Objects From Files
usersTab = pd.read_table('ml-1m/users.dat', '::', engine = 'python', names = ["User ID","Gender","Age","Occupation Code","Zip"])
ratingsTab = pd.read_table('ml-1m/ratings.dat', '::', engine = 'python', names = ["User ID","Movie ID","Rating","Timestamp"])
moviesTab = pd.read_table('ml-1m/movies.dat', '::', engine = 'python', names = ["Movie ID","Title","Genre"])

#Merge all the data into One Table
movie_data = pd.merge(usersTab, ratingsTab, on="User ID")
movie_data = pd.merge(movie_data, moviesTab, on="Movie ID")

#Make a Pivot Table and then sort it
#This will match the Movies with the total number of ratings they have
ptable = pd.pivot_table(movie_data, values="Rating", index=["Title"], aggfunc= lambda x: len(x))
ptable = ptable.sort(axis=0, inplace=False)

#Print off Top 5 Movies with the Most Ratings
print "Top 5 Movies with the Most Ratings"
print ptable[-5:]

#Find the first movie with atleast 250 ratings
for i in ptable:
	if ptable[i] >= 250:
		break 

#Then add all the movies at that idx and above to the Object "Active Titles"
active_titles = ptable[i:]

topThree = pd.pivot_table(movie_data, values=["Rating"], index=["Title"], columns=["Gender"], aggfunc= [np.mean,lambda x: len(x)])
topThree = topThree.sort_index(axis==0, inplace=False)
print topThree
