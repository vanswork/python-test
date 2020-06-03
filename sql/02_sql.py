### INSERT Command ###

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
# cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)""")

# insert data
try: 
	cursor.execute("INSERT INTO population VALUES('New York City8', 'NY', 8400000)")
	cursor.execute("INSERT INTO population VALUES('San Francisco9', 'CA', 800000)")

	cities = [
	('Boston', 'MA', 600000),
	('Chicago', 'IL', 2700000),
	('Houston', 'TX', 2100000),
	('Phoenix', 'AZ', 1500000)
	]

	emps = [
	('Van', 'Nguyen'),
	('Jamie', 'Nguyen'),
	('Matt', 'Snyder'),
	('Val', 'Snyder')
	]

	cursor.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
	cursor.executemany('INSERT INTO employees VALUES(?, ?)', emps)

	# commit the changes
	conn.commit()
except: 
	print("Ooops! I did it again")

# close the database connection
conn.close()