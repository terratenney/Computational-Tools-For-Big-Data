
# coding: utf-8

# In[12]:

#Checks if Node has even number of edges
def isEven(num):
		for node in num:
			if node[1] % 2 != 0:
				return False
		return True

#Opens text file and splits file to nodes
lines = sc.textFile("euler3.txt")
edges = lines.flatMap(lambda line: line.split())

#Counts how many times each node is mentioned to get degree
count = edges.map(lambda e: (e,1))
count = count.reduceByKey(lambda node, c: node + c)

#If node degree is even, then it has an Euler Tour
if isEven(count.collect()):
    print "Graph has an Euler Tour"
else:
    print "Graph does not have an Euler Tour"



# In[ ]:




# In[ ]:




# In[ ]:



