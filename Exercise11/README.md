This week I used Feature Hashing and Local Sensitive Hashing on a bag of words of various articles. I wrote a program that will predict whether a certain topic was "earn" based on the "body" of the articles given. I did this using multiple techniques. First I used a Random Forest Classifier and Feature Hashing. Then I used a MinHash technique. The articles are located in the json folder.

Exercise 1:

Load them into Python. Remove all articles that do not have at least one topic and a body. This should give you 10377 articles remaining.
Make a bag-of-words encoding of the body of the articles. Remember to lower-case all words. This should result in a matrix, with one row for each article (which has a topic) and one column for each unique word in those articles.
How many features/columns do you get in your term/document matrix from your bag-of-words encoding? One solution (mine) gives a matrix of size 10377 x 70794 (this is without removing punctuation).
Train a random forest classifier to predict if an article has the topic ‘earn’ or not from the body-text (encoded using bag-of-words). Use 80% of the data for training data and 20% for test data. Use 50 trees (n_estimators) in your classifier.
How does the classifier perform (how large a fraction of the documents in the test set are classified correctly)?
Now implement feature hashing and use 1000 buckets instead of the raw bag-of-words encoding.
How does this affect your classifier performance?

Exercise 2:

Implement your own MinHash algorithm.
Using the same dataset as before, hash the body of some of the articles (encoded using bag of words) using MinHash – to get the code to run faster, work with just 100 articles to begin with.
Try with different number of hash functions/permutations (for example 3, 5, 10).
Look at which documents end up in the same buckets. Do they look similar? Do they share the same topics?
