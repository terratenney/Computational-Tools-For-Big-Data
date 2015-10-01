#!C:/Users/Greg/Anaconda/Python
import time

#Simple Sum Function
def simplefunc():
	start_time = time.time() 
	for x in range(500):
		sum = 0.0
		for i in range(1,10001):
			sum += 1.0 / pow(i,2)
	print("----Python took %s seconds----" % (time.time()-start_time) );

 
#Function Call
simplefunc()
