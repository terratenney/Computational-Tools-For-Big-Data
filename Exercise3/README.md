Instructions for Exercise 3:

Exercise 3.1 (numpy):

Write a script which reads a matrix from a file and solves the linear matrix equation Ax=b where b is the last column of the input-matrix and A is the other columns. It is okay to use the solve()-function from numpy.linalg.

Exercise 3.2 (scipy):

Write a script that reads in a list of points (x,y), fits/interpolates them with a polynomial of degree 3. Solve for the (real) roots of the polynomial numerically using Scipy’s optimization functions (not the root function in Numpy).

Exercise 3.3 (pandas):

Do the first two exercises (Todo’s) at the bottom of http://byumcl.bitbucket.org/bootcamp2013/labs/pandas.html

Exercise 3.4 (scikit-learn):

Last week you read in a dataset for a Kaggle competition and created a bag-of-words representation on the review strings. Train a logistic regression classifier for the competition using your bag-of-words features (and possibly some of the others) to predict the variable “requester_received_pizza”. For this exercise, you might want to work a little bit more on your code from last week. Use 90% of the data as training data and 10% as test data.

How good is your classifier? Discuss the performance of the classifier.

Exercise 3.5 (cython):

Write a simple Python function for computing the sum \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \ldots with 10,000 terms (this should be around 1.644), 500 times in a row (to make the execution time measurable). Now compile the code with Cython and see how much speedup you can achieve by this.
