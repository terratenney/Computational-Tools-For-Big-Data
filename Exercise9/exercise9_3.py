
# coding: utf-8

# In[58]:

#Splits the line into whatever desired index
#This problem requires the bssid
def splitString(s,idx):
    line = s.split(',')
    return line[idx]

#Open the file and map each line to its bssid
network = sc.textFile("wifi.data")
network_obs = network.map(lambda x: splitString(x,1))

#Count the occurances of each bssid
count = network_obs.map(lambda net: (net,1))
count = count.reduceByKey(lambda net,c: net + c)

#Print off the 10 networks with the highest value
print "The 10 networks observed the most:"
count.takeOrdered(10, key=lambda x: -x[1])


# In[2]:

#Splits the line into whatever desired index
#This problem requires the ssid and bssid
def splitString(s,idx):
    line = s.split(',')
    return line[idx]

#Open the file of network connections
network = sc.textFile("wifi.data")
#Reduce each line to a new key of its (bssid,ssid)
#This will get us the unique networks and their names
common = common.reduceByKey(lambda net,value: (splitString(net,1),splitString(net,0)))

#Map and count each occurance of a network name
count = common.map(lambda name: (name[1],1))
count = count.reduceByKey(lambda name,c: name + c)

#Print off the top 10 names that occur
print "The 10 most common wifi names:"
count.takeOrdered(10, key=lambda x: -x[1])


# In[4]:

#Splits the line into whatever desired index
#This problem requires the ssid and bssid
def splitString(s,idx):
    line = s.split(',')
    return line[idx]

#Open the file of network connections
network = sc.textFile("wifi.data")
#Reduce each line to a new key of its (bssid,ssid)
#This will get us the unique networks and their names
common = common.reduceByKey(lambda net,value: (splitString(net,1),splitString(net,0)))

#Map and count each occurance of a network name
count = common.map(lambda name: (name[1],len(name[1])))

#Print off the top 10 longest names that occur
print "The 10 longest names:"
count.takeOrdered(10, key=lambda x: -x[1])


# In[ ]:



