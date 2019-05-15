import sys
import json
import mysql.connector
from flask import Flask, jsonify, request
#from bson.json_util import dumps

# App 
app = Flask(__name__)

# Database helper functions
#def jsonify_mongo(pymongo_object, status=200):
#	""" Converts from non-serializable Pymongo object to json """
#	return app.response_class(
#		response=dumps(pymongo_object),
#		status=status,
#		mimetype='application/json'
#	)

def initialize_db():
	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'shop_db'
	}

	

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	sql = "DELETE FROM cartItem;"
	cursor.execute(sql)
	connection.commit()
	sql = "DELETE FROM products;"
	cursor.execute(sql)
	connection.commit()
	sql = "INSERT INTO products (name, description, price, colour) VALUES ('rochie', 'lunga', 200, 'alba'), ('jeans', 'rupti', 150, 'albastrii'), ('tricou', 'mulat', 40, 'verde');"
	cursor.execute(sql)
	connection.commit()

	cursor.close()
	connection.close()

# Routes
@app.route('/products', methods=["GET"])
def get_books():
	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'shop_db'
	}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	sql = 'SELECT id, name, description, price, colour FROM products;' 
	print(sql)
	cursor.execute(sql)
	
	data = []
	#print("da")
	for (id, name, description, price, colour) in cursor:
		#print(name)
		data.append({'id': id, 'name': name, 'desc': description, 'price': price, 'colour': colour})
	
	cursor.close()
	connection.close()

	return json.dumps(data)

# Routes
@app.route('/cart/', methods=["GET"])
def get_cart():
	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'shop_db'
	}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	#sql = "SELECT cartItem.product_id as id, products.name as name, cartItem.quantity as quantity, cartItem.size as size FROM cartItem INNER JOIN products on cartItem.product_id=products.id;" 
	sql = "SELECT product_id as id, quantity, size FROM cartItem;"	
	print(sql)
	cursor.execute(sql)
	
	data = []
	print("da")
	for (id, quantity, size) in cursor:
		print(id)
		data.append({'id': id, 'name': '', 'quantity': quantity, 'size': size})
	
	cursor.close()
	connection.close()

	return json.dumps(data)


# Routes
@app.route('/orders', methods=["GET"])
def get_orders():

	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'shop_db'
	}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	sql = 'SELECT id, pay_amount, placement_date FROM orders ' 
	cursor.execute(sql)
	
	data = []
	for (order_id, pay_amount, placement_date) in cursor:
		data.append({'order_id': order_id, 'amount': pay_amount, 'date': placement_date})
	
	cursor.close()
	connection.close()

	return data


@app.route('/add_cart', methods=["GET", "POST"])
def add_cart():
	if request.method == "POST":
		json = request.get_json()

		prod_id = json['prod_id']
		quantity = json['quantity']
		size = json['size']

		print(prod_id)
		print(quantity)
		print(size)

		config = {
			'user': 'root',
			'password': 'root',
			'host': 'db',
			'port': '3306',
			'database': 'shop_db'
		}


		connection = mysql.connector.connect(**config)
		cursor = connection.cursor()
		sql = "INSERT INTO cartItem (product_id, size, quantity) VALUES (%s, %s, %s);" 
		val = (prod_id, size, quantity)
		cursor.execute(sql, val)
		connection.commit()
	
		cursor.close()
		connection.close()
		return jsonify(message="success")
	

if __name__ == '__main__':
	initialize_db()
	app.run(debug=True, host='0.0.0.0') 
