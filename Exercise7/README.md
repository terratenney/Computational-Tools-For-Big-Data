This week I wrote some streaming algorithms in Python for dealing with data that is too large to store.

Exercise 7.1

Implement a Bloom Filter as a Python class. The class should have an add method which adds a string to the filter, and a lookup method which determines if a string is “in the filter”. The number of hash-functions in the filter should be m/n * ln(2), where m is the size of the bit-array and n is the expected number of distinct items in the stream. Use a filter with 1 million bits.

Write a script which looks through the Shakespeare text-file and for each word in the file determines if it is in the English dictionary. You should use the dictionary.

What is the speed difference between this approach, and simply looping over the dictionary for each word in Shakespeare?

Which words are reported to be in the dictionary but are actually not in there?

Exercise 7.2

Implement the Flajolet-Martin algorithm to determine the number of distinct words in the Shakespeare file. You should implement it as a class with (at least) the two methods process(element) which reads in an element and adds it to the datastructure, and give_estimate() which gives an estimate of the amount of distinct elements processed.

The idea is to construct a class which does not need to store much, so make sure that you are not saving some large amount of elements in the class.

Note: Single cardinality estimates are prone to outliers. To improve the accuracy, follow the solution described in this wikipedia article under “Improving accuracy”. https://en.wikipedia.org/wiki/Flajolet%E2%80%93Martin_algorithm
