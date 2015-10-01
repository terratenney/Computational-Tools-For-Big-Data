import time
import Cython

#Faster Cython Function
def fastfunc():
	cdef float start_time = time.time()
	cdef int x
	cdef int i
	cdef float sum
	for x in range(500):
		sum = 0.0
		for i in range(1,10001):
			sum += 1.0 / pow(i,2)

	print("----Cython took %s seconds" % (time.time() - start_time) );

#Function call
#fastfunc()
