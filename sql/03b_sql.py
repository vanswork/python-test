# import from CSV

# import the csv library
import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# open the csv file and assign it to a variable
	employees = csv.reader(open("employees.csv", "rU"))

	# create a new table called employees
	# c.execute("CREATE TABLE employees7(firstname TEXT, lastname TEXT)")

	# insert data into table
	stmt = "INSERT INTO employees(firstname, lastname) values (?, ?)"
	c.executemany(stmt, employees)