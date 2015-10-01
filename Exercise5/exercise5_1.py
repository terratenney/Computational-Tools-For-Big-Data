#!C:/Users/Greg/Anaconda/Python

import sqlite3 as lite
import pymongo
from pymongo import MongoClient

#SQLite
print "SQLite"
#Connect to Database
conn = lite.connect("northwind.db")
#Establish Cursor
c = conn.cursor()

#Create new Test Table with some values
c.executescript("""
	DROP TABLE IF EXISTS Test;
    CREATE TABLE Test(Name TEXT, Number INT);
	INSERT INTO Test VALUES("Test1", 1);
	INSERT INTO Test VALUES("Test2", 2);
	INSERT INTO Test VALUES("Test3", 3);
	""")

c.execute("SELECT * FROM Test")

#Print them off
rows = c.fetchall()
for row in rows:
	print row

#commit them to the file
conn.commit()
conn.close()

#Mongo
print "Mongo:"
#Connect to client
client = MongoClient()

#Etablish client
db = client.Northwind

#Create test posts
posts = db.posts
new_posts= [{"author": "Test1",
          "text": "Another post!",
          "tags": ["bulk", "insert"]},
         {"author": "Test2",
          "title": "MongoDB is fun",
          "text": "and pretty easy too!"}]
print new_posts
result = posts.insert_many(new_posts)

#Print off posts and Insterted IDs
print new_posts
