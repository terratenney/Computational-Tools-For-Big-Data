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

#Check for Customer ID
t = ('ALFKI',)
c.execute("SELECT * FROM Orders WHERE CustomerID=?", t)

#Store ALFKI's products
products = []

rows = c.fetchall()
for row in rows:
	t2 = (row[0],)
	#Only Check orders with ALFKI's ID
	c.execute("SELECT * FROM 'Order Details' WHERE OrderID=?", t2)

	#Add ALFKIs products to array
	details = c.fetchall()
	for order in details:
		if order[1] not in products:
			products.append(order[1])

#Print off his purchases
print "ALFKI's purchases were: "
print products

#Go through orders with products similar to ALFKIs
c.execute("SELECT * FROM Orders")
orders = c.fetchall()
#People and orders
PnO = {}
#For every order, add the person to the dictionary, and keep track of their Order IDs
for o in orders:
	if o[1] not in PnO:
		if o[1] != "ALFKI":
			PnO[o[1]] = [o[0]]
	elif o[1] in PnO:
		PnO[o[1]].append(o[0])

#Customers with similar products
sim = []
#Go through dictionary and search for products in order details
for k,v in PnO.iteritems():
	types= []
	for o in v:
		t3 = (o,)
		c.execute("SELECT * FROM 'Order Details' WHERE OrderID=?", t3)
		prod = c.fetchall()
		for p in prod:
			#If the product is in ALFKIs products, add the type to array
			if p[1] in products:
				if p[1] not in types:
					types.append(p[1])

	if len(types) > 0:
		sim.append( (k, types) )

	

#Print off How many people had bought similar items
print "%d people bought similar items." % len(sim)
#Print off the Customer, how many similar items they bought, and what the similar items were
for p in sim:
	print "%s bought %d similar product types to ALFKI. They were: " % (p[0], len(p[1]))
	print p[1]

conn.close()



#Mongo
print "Mongo:"
#Connect to client
client = MongoClient()

#Etablish client
db = client.Northwind

#Store ALFKI's products
products = []

#Only Check orders with ALFKI's ID
collection_orders = db.orders
for id in collection_orders.find({"CustomerID": "ALFKI"}):
	order = id['OrderID']

	#Find all the products he bought with his orders
	order_details = db['order-details']
	for det in order_details.find({"OrderID": order}):
		if det['ProductID'] not in products:
			products.append(det['ProductID'])

print "ALFKI's purchases were: "
print products

#People and orders
PnO = {}
#For every order, add the person to the dictionary, and keep track of their Order IDs
for o in collection_orders.find():
	if o['CustomerID'] not in PnO:
		if o['CustomerID'] != "ALFKI":
			PnO[o['CustomerID']] = [o['OrderID']]
	elif o['CustomerID'] in PnO:
		PnO[o['CustomerID']].append(o['OrderID'])

#Customers with similar products
sim = []

order_details = db['order-details']
#Go through dictionary and search for products in order details
for k,v in PnO.iteritems():
	types = []
	for o in v:
		for prod in order_details.find({"OrderID": o}):
			#If the product is in ALFKIs products, add the type to array
			if prod["ProductID"] in products:
				if prod["ProductID"] not in types:
					types.append(prod["ProductID"])

	#If they have atleast 1 similar product, add to Similar array
	if len(types) > 0:
		sim.append( (k, types) )

#Print off How many people had bought similar items
print "%d people bought similar items." % len(sim)
#Print off the Customer, how many similar items they bought, and what the similar items were
for p in sim:
	print "%s bought %d similar product types to ALFKI. They were: " % (p[0], len(p[1]))
	print p[1]