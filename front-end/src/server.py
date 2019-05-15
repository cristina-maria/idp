import requests 
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for

BOOK_API_SERVER = os.environ['BOOK_API_SERVER']
app = Flask(__name__)

@app.route('/')
def show_products():
    products = requests.get(BOOK_API_SERVER + "/products").json()
    return render_template('show_products.html', products=products)

@app.route('/orders')
def show_orders():
    orders = requests.get(BOOK_API_SERVER + "/orders")
    return render_template('show_orders.html', orders=orders)

@app.route('/cart')
def show_cart():
    cart = requests.get(BOOK_API_SERVER + "/cart").json()
    return render_template('show_cart.html', cart=cart)


@app.route('/add_to_cart/')
def add_to_cart(product_id=0):
	print("da")
	json = {
		'prod_id': product_id,
		'quantity': 1,
		'size': 'S',
	}
	print(json['prod_id'])
	response = requests.post(BOOK_API_SERVER + "/add_cart", json=json)
	return "Succes"
	

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
