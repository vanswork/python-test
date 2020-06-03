### WITH STATEMENT ### 

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# insert multiple records using a tuple
	cities = [
	('Boston', 'MA', 600000),
	('Los Angeles', 'CA', 38000000),
	('Houston', 'TX', 2100000),
	('Philadelphia', 'PA', 1500000),
	('San Antonio', 'TX', 1400000),
	('San Diego', 'CA', 130000),
	('Dallas', 'TX', 1200000),
	('San Jose', 'CA', 900000),
	('Jacksonville', 'FL', 800000),
	('Indianapolis', 'IN', 800000),
	('Austin', 'TX', 800000),
	('Detroit', 'MI', 700000)
	]

	# insert data into table
	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities) # parametrized statements are the ??