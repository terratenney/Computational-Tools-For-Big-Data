#!/usr/bin/python

import numpy as np
from scipy.interpolate import UnivariateSpline

def interpolate( file ):
	openFile = open(file, "r")
	read_it = openFile.read()

	x = []
	y = []

	for line in read_it.splitlines():
		text = line.split()

		x.append( float(text[0]) )		#Add all x's to an array
		y.append( float(text[1]) )		#Add all y's to an array

	x = np.array(x)
	y = np.array(y)

	f = UnivariateSpline(x,y,k=3)			#Interpolate the points

	roots = f.roots()				#Find the roots
	print roots

	openFile.close();

#Function Call
interpolate("pointlist.txt")		
	
