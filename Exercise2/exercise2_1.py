#!/usr/bin/python
#First Method taking in file "matrix.txt" and printing list of lists

#Function1
def readmatrix( file ):
   list = open( file, 'r' )
   return list.readlines();

#Calling function
print readmatrix( 'matrix.txt' )


#Funtion2
def reverse( list, matrixfile ):
   file = open( matrixfile, 'w' )
   for i in list:
      file.write(i)
   file.close()
   return file;

#Calling function
reverse( readmatrix('matrix.txt'), 'output.txt' )
