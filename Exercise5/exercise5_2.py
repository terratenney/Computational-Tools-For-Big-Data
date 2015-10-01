#!C:/Users/Greg/Anaconda/Python

import sqlite3 as lite
import pymongo
from pymongo import MongoClient

#SQLite
print "SQLite:"
#Connect to Database
conn = lite.connect("northwind.db")
#Establish Cursor
c = conn.cursor()

#Check for Customer ID
t = ('ALFKI',)
c.execute("SELECT * FROM Orders WHERE CustomerID=?", t)

rows = c.fetchall()
for row in rows:
	t2 = (row[0],)
	#Only Check orders with ALFKI's ID
	c.execute("SELECT * FROM 'Order Details' WHERE OrderID=?", t2)

	#Print off Details of Order
	details = c.fetchall()
	for order in details:
		print ("CustomerID: %s. OrderID: %s. ProductID: %s." % (row[1], order[0], order[1]))

conn.close()


#Mongo
print "Mongo:"
#Connect to client
client = MongoClient()

#Etablish client
db = client.Northwind

collection_orders = db.orders
orderIDs = []
for order in collection_orders.find({"CustomerID": "ALFKI"}).sort("OrderID"):
	orderIDs.append(order["OrderID"])

order_details = db['order-details']
for order in range(len(orderIDs)):
	for det in order_details.find({"OrderID": orderIDs[order]}):
		print ("CustomerID: ALFKI. OrderID: %s. ProductID: %s." % (det["OrderID"], det["ProductID"]))
