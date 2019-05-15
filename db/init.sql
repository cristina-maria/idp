CREATE DATABASE shop_db;
use shop_db;

create table products(
	id int NOT NULL AUTO_INCREMENT,
	name varchar(30),
	description varchar(30),
	price int,
	colour varchar(30),
	PRIMARY KEY (id)	
);

create table orders(
	id int NOT NULL AUTO_INCREMENT,
	placement_date varchar(10),
	pay_amount int,
	PRIMARY KEY (id)
);

create table cartItem(
	id int NOT NULL AUTO_INCREMENT,
	product_id int,
	quantity int,
	size varchar(5),
	PRIMARY KEY (id)
);
