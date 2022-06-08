import mysql.connector

user = 'root'
password = 'password'
# database = 'yelp'

# conn = mysql.connector.connect(user=user, passwd=password, database=database)
conn = mysql.connector.connect(user=user, passwd=password)
cur = conn.cursor()

sql = 'DROP DATABASE IF EXISTS yelp'
cur.execute(sql)

sql = 'CREATE DATABASE IF NOT EXISTS yelp CHARACTER SET utf8 collate utf8_general_ci;'
cur.execute(sql)

sql = 'USE yelp'
cur.execute(sql)

sql = 'DROP TABLE IF EXISTS business'
cur.execute(sql)

sql = 'DROP TABLE IF EXISTS review'
cur.execute(sql)

sql = 'DROP TABLE IF EXISTS tip'
cur.execute(sql)

sql = '''CREATE TABLE IF NOT EXISTS business (
	bid VARCHAR(30),
	name TEXT,
	city VARCHAR(255),
	state VARCHAR(10),
	stars FLOAT,
	review_count INT,
	categories TEXT,
	PRIMARY KEY (bid)
) character set utf8 collate utf8_general_ci'''
cur.execute(sql)

sql = '''CREATE TABLE IF NOT EXISTS review (
	rid VARCHAR(30),
	uid VARCHAR(30),
	bid VARCHAR(30),
	star INT,
	text TEXT,
	PRIMARY KEY (rid),
	FOREIGN KEY (bid) REFERENCES business(bid) ON DELETE CASCADE
) character set utf8 collate utf8_general_ci'''
cur.execute(sql)

sql = '''CREATE TABLE IF NOT EXISTS tip (
	text TEXT,
	compliment_count INT,
	bid VARCHAR(30),
	uid VARCHAR(30),
	FOREIGN KEY (bid) REFERENCES business(bid) ON DELETE CASCADE
) character set utf8 collate utf8_general_ci'''
cur.execute(sql)


conn.commit()
conn.close()
