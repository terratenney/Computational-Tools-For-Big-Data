#!/usr/bin/python

#Takes integer N and outputs all bit strings length N
def bit_strings( N ):
   count = 0

   #2^N lists
   out_num = pow(2,N)
   list = []

   #Using format-function, you can convert integer into binary
   #Then add to the list
   while (count < out_num):
      list.append(["{0:{fill}{width}b}".format(count,width=N,fill=0)])
      count += 1
   print list;

#Function test
num = raw_input('Enter an integer N: ')
num = int(num)
   
bit_strings(num)
