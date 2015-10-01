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

#Order ID's, Customer ID's
orderIDs = []
custIDs = {}

#Check for Customer ID
t = (7,)
c.execute("SELECT * FROM 'Order Details' WHERE ProductID=?", t)

#Get all Order IDs from ProductID == 7
rows = c.fetchall()
for row in rows:
	orderIDs.append(row[0])

#Go into the table "Orders" and collect the Customer ID using the Order ID
for id in orderIDs:
	t2 = (id,)
	c.execute("SELECT * FROM Orders WHERE OrderID=?", t2)

	details = c.fetchone()
	if details[1] not in custIDs.keys():
		#(CustomerID, [Orders Made])
		custIDs[details[1]] = []

#Collect Order IDs made by that customer
for cust,v in custIDs.iteritems():
	t3 = (cust,)
	c.execute("SELECT * FROM Orders WHERE CustomerID=?", t3)

	purchases = c.fetchall()

	for p in purchases:
		v.append(p[0])

#Total items bought other than ProductID == 7
totalitems = []

#Use each customers OrderID to find the ProductIDs purchased
for person,v in custIDs.iteritems():
	prodIDs = []
	for order in v:
		t4 = (order,)
		c.execute("SELECT * FROM 'Order Details' WHERE OrderID=?", t4)
		prod = c.fetchall()
		for p in prod:
			if p[1] != 7:
				prodIDs.append(p[1])
				if p[1] not in totalitems:
					totalitems.append(p[1])

	#print ("%s also bought %d other items. They were Product ID's: " % (person[0], len(person[1])) )
	#print prodIDs

#Print total number of different products purchased and Product IDs
print "People also bought %d other items. They were: " % len(totalitems)
print totalitems
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

#Collect all the Order IDs and Quantities from Product ID = 7
order_details = db['order-details']
for det in order_details.find({"ProductID": 7}):
	orderIDs.append(det['OrderID'])

#Find Customer IDs in orders file, using Order IDs
collection_orders = db.orders
for order in range(len(orderIDs)):
	for customer in collection_orders.find({"OrderID": orderIDs[order]}):
		custIDs[customer['CustomerID']] = []

		for id in collection_orders.find({"CustomerID": customer['CustomerID']}):
			custIDs[customer['CustomerID']].append(id["OrderID"])

#Total items bought other than ProductID == 7
totalitemsM = []

for person,v in custIDs.iteritems():
	prodIDs = []
	for ord in v:
		for purchase in order_details.find({"OrderID": ord}):
			if purchase["ProductID"] != 7:
				prodIDs.append(purchase["ProductID"])
				if purchase["ProductID"] not in totalitemsM:
					totalitemsM.append(purchase["ProductID"])

	#print ("%s also bought %d other items. They were Product ID's: " % (person[0], len(person[1])) )
	#print prodIDs

#Print total number of different products purchased and Product IDs
print "People also bought %d other items. They were: " % len(totalitemsM)
print totalitemsM
