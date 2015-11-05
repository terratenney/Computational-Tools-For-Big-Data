This week, I did various exercises implementing Apache Spark. I used the 'Vagrant' virtual machine iPython notebooks to perform all of these. This came with Pyspark and other tools. I have included some of the test files I used as well.

Exercise 1:

Write a Spark job to count the occurrences of each word in a text file. Document that it works with a small example.

Exercise 2:

Write a Spark job that determines if a graph has an Euler tour (all vertices have even degree) where you can assume that the graph you get is connected. This file https://www.dropbox.com/s/usdi0wpsqm3jb7f/eulerGraphs.txt?dl=0 has 5 graphs – for each graph, the first line tells the number of nodes N and the number of edges E. The next E lines tells which two nodes are connected by an edge. Two nodes can be connected by multiple edges.

euler.txt files

Document that it works using a small example.

Exercise 3:

You are given a couple of hours of raw WiFi data from my phone: 'wifi.data'

Compute the following things using Spark:

1. What are the 10 networks I observed the most, and how many times were they observed? Note: the bssid is unique for every network, the name (ssid) of the network is not necessarily unique.
2. What are the 10 most common wifi names? (ssid)
3. What are the 10 longest wifi names? (again, ssid)
