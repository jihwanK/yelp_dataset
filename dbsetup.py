import mysql.connector

user = 'root'
password = 'password'
database = 'yelp'

conn = mysql.connector.connect(user=user, passwd=password, database=database)
cur = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS business (
	bid VARCHAR(30),
	name MIDTEXT,
	city VARCHAR(255),
	state VARCHAR(10),
	stars FLOAT,
	review_count INT,
	categories MIDTEXT,
	PRIMARY KEY (bid)
)'''
cur.execute(sql)

sql = '''CREATE TABLE IF NOT EXISTS review (
	rid VARCHAR(30),
	uid VARCHAR(30),
	bid VARCHAR(30),
	star INT,
	text MIDTEXT,
	PRIMARY KEY (rid),
	FOREIGN KEY (bid) REFERENCE business(bid) ON DELETE CASCADE
)'''
cur.execute(sql)

sql = '''CREATE TABLE IF NOT EXISTS tip (
	text MIDTEXT,
	compliment_count INT,
	bid VARCHAR(30),
	uid VARCHAR(30),
	FOREIGN KEY (bid) REFERENCE business(bid) ON DELETE CASCADE
)'''
cur.execute(sql)


conn.commit()
conn.close()