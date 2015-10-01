#!C:/Users/Greg/Anaconda/Python

import sqlite3 as lite
import pymongo
from pymongo import MongoClient

#SQLite
print "SQLite:"
#Connect to Database
conn = lite.connect("northwind.db")
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
#Establish Cursor
c = conn.cursor()

#Order ID's, Customer ID's and Quantities
orderIDs = []
custIDs = {}
quantity = []

#Check for Customer ID
t = (7,)
c.execute("SELECT * FROM 'Order Details' WHERE ProductID=?", t)

#Get all Order IDs and Quantities from ProductID == 7
rows = c.fetchall()
for row in rows:
	orderIDs.append(row[0])
	quantity.append(row[3])

#Go into the table "Orders" and collect the Customer ID using the Order ID
for id in range(len(orderIDs)):
	t2 = (orderIDs[id],)
	c.execute("SELECT * FROM Orders WHERE OrderID=?", t2)

	details = c.fetchone()
	if details[1] not in custIDs.keys():
		custIDs[details[1]] = quantity[id]
	else:
		custIDs[details[1]] += quantity[id]

#Print off each Customer with each Order and the Quantity of each
for person,v in custIDs.iteritems():
	print ("CustomerID: %s. Quantity: %s." % (person, v) )

conn.close()



#Mongo
print "Mongo:"
#Connect to client
client = MongoClient()

#Etablish client
db = client.Northwind

#Order ID's, Customer ID's and Quantities
orderIDs = []
custIDs = {}
quantity = []

#Collect all the Order IDs and Quantities from Product ID = 7
order_details = db['order-details']
for det in order_details.find({"ProductID": 7}):
	orderIDs.append(det['OrderID'])
	quantity.append(det['Quantity'])

#Find Customer IDs in orders file, using Order IDs
collection_orders = db.orders
for order in range(len(orderIDs)):
	for customer in collection_orders.find({"OrderID": orderIDs[order]}):
		if customer not in custIDs.keys():
			custIDs[customer['CustomerID']] = quantity[order]
		else:
			custIDs[customer['CustomerID']] += quantity[order]

#Print off each Customer with each Order and the Quantity of each
for person,v in custIDs.iteritems():
	print ("CustomerID: %s. Quantity: %s." % (person, v) )
