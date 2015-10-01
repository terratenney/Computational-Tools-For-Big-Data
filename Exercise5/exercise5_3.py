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
	#If greater than or equal to 2 products
	if len(details) >= 2:
		for order in details:
			print ("CustomerID: %s. OrderID: %s. ProductID: %s." % (row[1], order[0], order[1]))

conn.close()


#Mongo
print "Mongo:"
#Connect to client
client = MongoClient()

#Etablish client
db = client.Northwind

#Get from file "orders"
collection_orders = db.orders

#Save all the orderIDs from ALFKI
orderIDs = []
for order in collection_orders.find({"CustomerID": "ALFKI"}):
	orderIDs.append(order["OrderID"])

#For every order, print off the order ID and product ID, from file "order-details"
order_details = db['order-details']
for order in range(len(orderIDs)):
	for det in order_details.find({"OrderID": orderIDs[order]}):
		#If greater than or equal to 2 products
		if order_details.find({"OrderID": orderIDs[order]}).count() >= 2:
			print ("CustomerID: ALFKI. OrderID: %s. ProductID: %s." % (det["OrderID"], det["ProductID"]))