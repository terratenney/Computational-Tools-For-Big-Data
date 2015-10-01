#!C:/Users/Greg/Anaconda/Python

import cPickle as pickle
import numpy as np
import time
from scipy.sparse import csr_matrix

start_time = time.time()

#DBSCAN Function
def DB(epsilon, M, pointIdx):
 	
	#Cluster number
	C = 0
	
	#Scan every point in our Data
	for p in dataMatrix:

		#If it has not been visited, mark as visited
		if pointIdx not in visited:
			visited.append(pointIdx)

			#Collect nearest neighbors of point
			neighbors = point_neighbors[pointIdx]

			#If length of nearest neighbors is less than Minimum number of points, add to noise
			if len(neighbors) < M:
				noise.append(pointIdx)
				been_clustered.append(pointIdx)

			#Otherwise increment cluster number and expand cluster
			else:
				C += 1
				expandClust(pointIdx, neighbors, C, epsilon, M)
	
		#Move on to next point
		pointIdx += 1;

#Cluster points
def expandClust(p, neighborPts, C, epsilon, M):
	
	#Define cluster with cluster number and indices of points in that cluster
	cluster = (C, [])
	#Add to array of clusters
	allclusters.append(cluster)	

	#Cluster all neighbors
	while len(neighborPts) > 0:

		#If neighbor hasn't been visited, mark as visited
		if neighborPts[0] not in visited:
 			visited.append(neighborPts[0])

			#Collect new neighbors
			new_neighbors = point_neighbors[neighborPts[0]]
			
			#If number of neighbors is greater than or equal to minimum number of points, combine them
			if len(new_neighbors) >= M:
				neighborPts = combine(neighborPts, new_neighbors)
	
		#Check if point has been previously clustered, if not cluster it		
		if neighborPts[0] not in been_clustered:
			cluster[1].append(neighborPts[0])
			been_clustered.append(neighborPts[0])
		
		#Remove points from neighbors
		neighborPts = neighborPts[1:];
			
#Returns combination of x and y
def combine(x,y):
	z = x
	for p in y:
		if p not in x:
			z = np.append(z,p)
	return z;

#Finds nearest neighbors for every point and stores in an array
#Using Jaccard Distance
def regionQuery(epsilon):

	for p in dataMatrix:
		rIdx = 0	
		result = []
		for d in dataMatrix:
			temp1 = d.indices
			temp2 = p.indices
			
			iter = np.intersect1d(temp1, temp2)
			union = np.union1d(temp1, temp2)

			if len(union) == 0:
				dist = 1
			else:
				dist = 1 - (len(iter)) / float(len(union))

			if dist <= epsilon:
				result.append(rIdx)
			rIdx += 1
		point_neighbors.append(result);


#Find size of largest cluster
def findlarge():
	largest = 0
	for clust in allclusters:
		if len(clust[1]) > largest:
			largest = len(clust[1])
	return largest;
	




#Array of visited point indices
visited = []
#Array of point indices that are noise
noise = []
#Array of all the clusters
allclusters = []
#Array of Point indices that have been clustered
been_clustered = []

#Loading our Data from a file into a matrix
dataMatrix = pickle.load(open("data_1000points_1000dims.dat", "rb"))
dataMatrix = csr_matrix(dataMatrix)

#Point index
pIdx = 0

#Neighbors of each point, each index is the point index, and each index will hold an array of the neighbors
point_neighbors = []

#Collect Point Distances
regionQuery(0.15)

#DBScan with parameters (Epsilon, Minimum number of Points, Point index)
DB(0.15, 2, pIdx)

#Size of largest cluster, not counting noise
largestClust = findlarge()

#Add noise to total clusters
allclusters.append( ("Noise", noise) )

#Output
print "There are %d Clusters" % len(allclusters)
print "The size of the largest Cluster is %d" % largestClust
#Run time
print("--- %s seconds ---" % (time.time() - start_time))

