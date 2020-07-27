# project/db_create.py
from views import db
from models import Task
from datetime import date


# create the database and the db table
db.create_all()  # initialize the database schema (i.e. Task) by calling db.create_all()

# insert data
# db.session.add(Task("Finish this tutorial", date(2016, 9, 22), 10, 1))
# db.session.add(Task("Finish Real Python", date(2016, 10, 3), 10, 1))

# commit the changes
db.session.commit()


""" Old method with sqlimport

with sqlite3.connect(DATABASE_PATH) as connection:
 
    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    # c.execute(""""""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL,
        status INTEGER NOT NULL)"""""")

    # insert dummy data into the table
    c.execute(
    'INSERT INTO tasks (name, due_date, priority, status)'
    'VALUES("Finish this tutorial", "03/25/2015", 10, 1)'
    )
    c.execute(
    'INSERT INTO tasks (name, due_date, priority, status)'
    'VALUES("Finish Real Python Course 2", "03/25/2015", 10, 1)'
    )
"""