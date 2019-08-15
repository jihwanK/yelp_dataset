import mysql.connector

user = 'root'
password = 'password'
# database = 'yelp'

# conn = mysql.connector.connect(user=user, passwd=password, database=database)
conn = mysql.connector.connect(user=user, passwd=password)
cur = conn.cursor()

sql = 'DROP DATABASE yelp'
cur.execute(sql)

sql = 'CREATE DATABASE IF NOT EXISTS yelp CHARACTER SET utf8 collate utf8_general_ci;'
cur.execute(sql)

sql = 'USE yelp'
cur.execute(sql)

sql = 'DROP TABLE business'
cur.execute(sql)

sql = 'DROP TABLE review'
cur.execute(sql)

sql = 'DROP TABLE tip'
cur.execute(sql)

sql = '''CREATE TABLE IF NOT EXISTS business (
	bid VARCHAR(30),
	name MIDTEXT,
	city VARCHAR(255),
	state VARCHAR(10),
	stars FLOAT,
	review_count INT,
	categories MIDTEXT,
	PRIMARY KEY (bid)
) character set utf8 collate utf8_general_ci'''
cur.execute(sql)

sql = '''CREATE TABLE IF NOT EXISTS review (
	rid VARCHAR(30),
	uid VARCHAR(30),
	bid VARCHAR(30),
	star INT,
	text MIDTEXT,
	PRIMARY KEY (rid),
	FOREIGN KEY (bid) REFERENCE business(bid) ON DELETE CASCADE
) character set utf8 collate utf8_general_ci'''
cur.execute(sql)

sql = '''CREATE TABLE IF NOT EXISTS tip (
	text MIDTEXT,
	compliment_count INT,
	bid VARCHAR(30),
	uid VARCHAR(30),
	FOREIGN KEY (bid) REFERENCE business(bid) ON DELETE CASCADE
) character set utf8 collate utf8_general_ci'''
cur.execute(sql)


conn.commit()
conn.close()