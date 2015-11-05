
# coding: utf-8

# In[29]:

import string

#Open text file and remove punctuation and set to lower case
lines = sc.textFile("test1.txt")
punc = lines.map(lambda text: text.lower())
punc = punc.map(lambda text: text.translate({ord(c): None for c in string.punctuation}))
#Split lines into words
split = punc.flatMap(lambda line: line.split())

#Map each word to a count of 1
words = split.map(lambda w: (w,1))
#Then count each occurance of a word
word_count = words.reduceByKey(lambda w, c: w + c)
word_count.collect()


# In[ ]:



