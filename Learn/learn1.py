import sqlite3
import re
import numpy
from urllib.request import urlopen

#################### Strings ######################

flavor = "apple pie"
phrase = flavor[1]
print(phrase)

strWord = type("Hello World")
print(strWord)

string1 = 'Hello World'
string2 = "1234"
string3 = "We're #1"
string4 = 'I said, "put it over by the llama."'

string5 = len("abc")
print(string5)

paragraph = "This planet has - or rather had - a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy."

print(paragraph)

paragraph = """This planet has - or rather had - a problem, which was
this: most of the people living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concerned with the movements of small
green pieces of paper, which is odd because on the whole it wasn't
the small green pieces of paper that were unhappy."""

print(paragraph)

string1 = "abra"
string2 = "cadabra"
magic_string = string1 + " " + string2
print(magic_string)

flavor = "apple pie"
print(flavor[0])
print(flavor[1])
print(flavor[-2])

final_index = len(flavor) - 1
print(final_index)
last_character = flavor[final_index]
print(last_character)

first_three_letters = flavor[0] + flavor[1] + flavor[2]
print(first_three_letters)
print(flavor[0:3])
print(flavor[:5])
print(flavor[5:])
print(flavor[:])
print(flavor[13:15])
print(flavor[-9:-6])
print(flavor[0])
print(flavor[-9:0])
print(flavor[-9:])

word = "goal"
word = "f" + word[1:]
print(word)

print("Jean-luc Picard".lower())
name = "Van Nguyen"
print(name.lower())
name2 = "van nguyen  "
print(name2.upper())
print(len(name2))

print(name2.rstrip())
print(name2.lstrip())
print(name2.strip())

starship = "Enterprise"
print(starship.startswith("En"))
print(starship.endswith("se"))

#################### Input Prompts ######################

prompt = "Hey, what's up? "
'''user_input = input(prompt)'''
'''print("You said:", user_input.upper())'''

prompt = "Yes or No? "
'''user_input = input(prompt)'''
'''print("The first letter you entered was " + user_input[0]'''

#################### Numbers ######################

num = "12"
print(num + num)
num = num + num
print(num)
print(num * 3)

n = 3
m = 4
print(f"{n} times {m} is {n * m}")

my_story = "I'm telling you the truth; nothing but the truth!"
my_story = my_story.replace("the truth", "lies")
print(my_story)

'''prompt = "Enter some text:"
user_input = input(prompt)
user_input = user_input.replace("a", "4")
user_input = user_input.replace("b", "8")
user_input = user_input.replace("l", "1")
user_input = user_input.replace("o", "o")
user_input = user_input.replace("s", "5")
user_input = user_input.replace("t", "7")
user_input = user_input.replace("e", "3")
print(user_input)'''

print(int(23434234242342352454352353252342342342342343))
print(float(100000.0))
print(int(1_000_000_000))
print(1e6)
print(float(20000000000000000000))
print(1e-4)

'''page 110'''

n = 2e400
print(n)

'''page 111 review exercises'''

num1 = 25000000
num2 = 25e-6

print(num1)
print(num2)

'''page 122'''

print(round(2.3))
print(round(3.5))
print(round(3.5232, 2))

print(abs(-5))
print(pow(2, 3))
print(pow(2, -2))
print(pow(2, 3, 2))  # same as (x ** y) % z

print("hi")

''' this is not working
num = 2
print(num.is_integer())
num = 2
print(num.is_integer())
'''

# page 129

n = 7.125
print(f"the value of n is {n}")  # 7.125
print(f"the value of n is {n: .2f}")  # 7.12
n = 342342343
print(f"the value of n is {n:,}")  # adds commas
n = .9
print(f"the value of n is {n: .1%}")  # 90.0%
print(f"the value of n is {n: .2%}")  # 90.00%

# complex numbers
n = 1 + 2j
print(n)  # (1+2j)
print(n.real)  # 1.032
print(n.imag)  # 2.0
print(n.conjugate())  # (1-2j)

#################### Functions ######################


# page 141

def multiply(x, y):
    """I do math"""
    product = x * y
    return product


help(multiply)


def ftempTOctemp(fTemp):
    """convert temperature F to C"""
    C = (fTemp - 32) * 5 / 9
    return int(C)


# prompt = "Enter a temperature in F: "
# user_input = input(prompt)
# print(ftempTOctemp(int(user_input)))

#################### Loops ######################

n = 1
while n < 5:
    print(n)
    n = n + 1

# num = float(input("Enter a positive number: "))
num = 5
while num <= 0:
    print("That's not a positive number!")
    num = float(input("Enter a positive number: "))

# page 157

# prints each letter in python
for letter in "Python":
    print(letter)

# same as above:
index = 0
word = "Python"
while index < len(word):
    print(word[index])
    index = index + 1

# prints python 3x (cycles through 0, 1, 2)
for n in range(3):
    print("python")

# starting point is 10, and ranges up to 19
# this multiples 10x10, then 11x11, and so on up to 19
for n in range(10, 20):
    print(n)
    print(n * n)

for n in range(1, 4):
    for j in range(4, 7):
        print(f"n = {n} and j = {j}")


def invest(amount, rate, years):
    totalAmount = amount
    for n in range(1, years + 1):
        totalAmount = totalAmount * (1 + rate)
        print(f"year {n}: ${totalAmount: .2f}")


print(invest(100, .05, 4))

# page 164: Scopes

total = 0


def add_to_total(n):
    global total  # uses the total variable in the global scope
    total = total + n


add_to_total(5)
print(total)

print("end success")

# LEGB
# if a function can't find the local scope, it goes up in heirarchy to find the variable until it finds it.
# Local Scope = current function, or top level scope of a script
# Enclosing Scope = scope one level up
# Global Scope = top most socpe.
# Build-in Scope = names of keywords
x = "Hello World"


def func():
    x = 2
    print(f"Inside 'func', x has the value {x}")


func()
print(f"Outside 'func', x has the value {x}")
# prints x = 2
# prints x = Hello World


# Break the rules
# When inside a function, and you have total = total + 1, this will cause an error because you are trying to assign "total" to something.
# This works though, def blah, blah = total + 1
# or use global total, then total + total = 1
total = 0


def add_to_total(n):
    total = total + n
    add_to_total(5)
    print(total)


# Chapter 7: Findinga nd Fixing code in bugs
# page 171

# see webadmin.py for debugging
# 1. guess where the bug is located
# 2. set a breakpoint and inspect the code
# 3. Identify the error and attempt to fix it
# 4. Repeat steps 1-3 until the error is fixed

# Chapter 8: Conditional Logic and Control Flow

# Chapter 9: Tuples, Lists

#################### TUPLES ######################
my_tuple = (1, 2, 3)
my_tuple2 = tuple("Python")
print(my_tuple2[2:4])
my_tuple3 = 1, 2
print("my_tuple3")
x, y = my_tuple3
print('x')  # prints 1
print("y")  # prints 2
print("x" in my_tuple3);

#################### LISTS ######################

# pg 246 Lists
colors = ["red", "yellow", "green", "blue"]
color1 = list("red")  # ['r','e','d']

# nesting 257
two_by_two = [[1, 2], [3, 4]]
two_by_two[0]  # prints [1,2]
two_by_two[1][0]  # prints 3

# copy lists
animals = ["lion" "tiger", "frmuious bandersnatch"]
large_cats = animals
large_cats.append("Tigger")
print(large_cats)  # prints ["lion" "tiger", "frmuious bandersnatch", "tigger"]
print(animals)  # prints ["lion" "tiger", "frmuious bandersnatch", "tigger"]

large_cats = animals[:]  # retains animals list as is unlike above example
large_cats.append("Tigger")
print(large_cats)  # prints ["lion" "tiger", "frmuious bandersnatch"]
print(animals)  # prints ["lion" "tiger", "frmuious bandersnatch", "tigger"]

#################### Dictionaries ######################

# dictionaries p265
contacts = {
    "Jenny": {"cell": "555-0199", "home": "867-5309"},
    "Mike": {"home": "281-554-5212"}
}

# pg 273
print(contacts["Jenny"]["cell"])

# copying lists, tuples
# a = list(b)  # doesn't affect b, and creates 2 unique identities
a = (1, 2, 3)  # a tuple
b = tuple(a)  # a and b are the same unique identities now

scores = {"David": 100, "Dan": 150, "Fletcher": 175}
scores_ist = []
print(list(scores.items()))  # returns a list of pairs (('David'), 100), ("Dan", 150), ('Fletcher', 175))


#################### OOP ######################

# pg285 OBJECT ORIENTED PROGRAMMING

# classes are blue prints
# classes contain special function, called instance METHODS.
# This defines behaviors and actions that an object can perform with its data

# properties / instance attributes = belong  to a specific object
# instance methods = functions that belong to a class and defined inside in a class
# class attributes = the same for all instances

# instantiating = creating new object instance from blue print

# 292
class Dog:
    species = "Canis familiaris"

    def __init__(self, name3, age):  # this is an instance METHOD (special function)
        self.name3 = name3  # creates a CLASS ATTRIBUTE called name3
        self.age = age

    # instance method
    def __str__(self):
        return f"{self.name3} is {self.age} years old"

    # instance method
    def description(self):
        return f"{self.name3} is {self.age} years old"

    # instance method
    def speak(self, sound):
        return f"{self.name3} barks {sound}"


buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)  # instantiate class Dog and populate with data

print(buddy.name3)
print(miles.age)
print(buddy.species)
print(miles.species)

print(miles.description())  # call instantiated object, and call the instance method description
print(miles.speak("Woof Woof"))
print(miles)  # calls __str__(self) instance method


#################### INHERIT FROM OTHER CLASSES ######################

# pg 301 Inherit From other classes

# Uses Dog Class

class JackRussellTerrier(Dog):  # pass the parent class as an argument
    def speak(self, sound="Arf"):
        # return f"{self.name3} says {sound}"
        return super().speak(sound)  # Python searches the parent class, Dog, for a .speak()




class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
lucky = GoldenRetriever("Herlihy", 2)

print(buddy.name3)
print(jack)  # prints __str_
print(type(miles))  # shows which class a given object belongs to
print(isinstance(miles, Dog))  # determines if miles is also an instance of the Dog class
print(isinstance(miles, JackRussellTerrier))  # determines if miles is also an instance of the JackRussellTerrier class
print(miles.speak())  # defaults to "Arf"
print(miles.speak("XY"))
print(lucky.speak())


#  pg 307. Exercise 2: Create Rectangle Class

class Rectangle:

    def __init__(self, length, width):
        self.length = length  # creates a CLASS ATTRIBUTE named length
        self.width = width

    def __str__(self):
        return f"{self.length} x {self.width}"

    def area(self, side_length):
        area1 = side_length * self.width
        return f"{area1}"


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)


    def area(self, side_length=4):
        self.side_length = side_length
        return super().area(side_length) # looks at parent class for .area method



mySquare = Square(4, 4)
print(mySquare.area(6))
print(f"{mySquare.length} a")
print(f"{mySquare.width} b")
print(f"{mySquare.side_length} c")

#################### FILE INPUT / OUTPUT ######################

# page 311 File Input and Output

output_file = open("hello.txt", "w")
output_file.writelines("This is my first file.")
output_file.close()

output_file = open("hello.txt", "a")

lines_to_write = [
    "\nThis is my file.",
    "\nThere are many like it,",
    "\nbut this one is mine.",
]

output_file.writelines(lines_to_write)
output_file.close()

input_file = open("hello.txt", "r")
# print(input_file.readlines())  # prints as list/tuple

# for line in input_file:  # print each line one by one instead of a list/tuple
#     print(line, end="") # Output an empty string when done printing

line = input_file.readline()  # read first line
while line != "":
    print(line, end="")
    line = input_file.readline()  # read the next line

input_file.close

# STORE FILE IN A LIST USING READLINES method
input_file = open("hello.txt", "r")
lines_in_file = input_file.readlines()

print("First Pass: ")
for line in lines_in_file:
    print(line, end="")

print("Second Pass: ")
for line in lines_in_file:
    print(line, end="")
input_file.close()

# 320

# USE WITH for file operations: opens file, sets it to a variable, and auto closes file

with open("hello.txt", "r") as input_file:
    for line in input_file.readlines():
        print(line, end="")

# opens a file and wwrites its contents out to a new file

with open("hello.txt", "r") as source, open("hi.txt", "w") as dest:
    for line in source.readlines():
        dest.write(line)

# pg 345 PIPS



# pg 323
# Working with Paths in Python

#################### DATABASES ######################

# pg 330
# DATABASES


connection = sqlite3.connect("test_database.db")
query = "SELECT datetime('now', 'localtime');"
cursor = connection.cursor()
print(cursor.execute(query))
print(cursor.fetchone())  # obtains top first row and stores in tuple
time = cursor.execute(query).fetchone()[0]  # chains two lines into one and returns top row into a string
print(time)
connection.close()

#  Use with command to have the connection auto closed
with sqlite3.connect("test_database2.db") as connection2:
    cursor2 = connection2.cursor()
    cursor2.executescript(
        """DROP TABLE IF EXISTS People;
            CREATE TABLE People(
                FirstName TEXT,
                LastName TEXT,
                Age INT
            );"""
    )

    cursor2.execute(
        """INSERT INTO People VALUES(
            'Ron',
            'Obvious',
            42
            );"""
    )
    people_values = (
        ("Luigi", "Vercotti", 43),
        ("Arthur", "Belling", 28)
    )
    cursor2.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)

    # cursor2.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?;",
    #                (45, 'Ron', 'Obvious'))

    query2 = "SELECT * FROM People"
    # time2 = cursor2.execute(query2).fetchone()[2]  # Execute query and fetch top row returned in one line
    cursor2.execute(query2)

    for row in cursor2.fetchall():  # Return each record from the executed query
        print(row)

# print(time2)

print("\nend!")


#################### Parse Websites ######################

# pg 403
# PARSE WEBSITES

url = "http://olympus.realpyton.org/profiles/aphrodite"
html_page = urlopen(url)
html_text = html_page.read().decode("utf-8")

print(html_text)

#################### Regular Expressions ######################

# pg 408 REGULAR EXPRESSIONS

regexptest = re.findall("ab*c", "ac", re.IGNORECASE)  # matches where string begins with a and ends with c, and has 0 or more b, between a and c
print(regexptest)

#  pg 419
# Interact with HTML Forms

#################### NUMPY ######################

# pg 43 NumPy

# Create an numpy array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

#################### Python Book 2 ######################
#################### Python Book 2 ######################
#################### Python Book 2 ######################

# pg 68

#################### Database stuff ######################

# import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
try: 
    cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)""")

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

    # select and print data
    cursor.execute("SELECT firstname, lastname from employees")
    rows = cursor.fetchall()
    # output the rows to the screen, row by row
    for r in rows:
        print(r[0], r[1])

    # commit the changes
    conn.commit()
except: 
    print("Ooops! I did it again")

# close the database connection
conn.close()


### SQLite Functions ###

# import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # create a dictionary of sql queries
    sql = {'average': "SELECT avg(population) FROM population",
    'maximum': "SELECT max(population) FROM population",
    'minimum': "SELECT min(population) FROM population",
    'sum': "SELECT sum(population) FROM population",
    'count': "SELECT count(city) FROM population"}

    # run each sql query item in the dictionary
    for keys, values in sql.items():

        # run sql
        c.execute(values)

        # fetchone() retrieves one record from the query
        result = c.fetchone()

        # output the result to screen
        print(keys + ":", result[0])


### import from CSV ###

# import csv
# import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # open the csv file and assign it to a variable
    employees = csv.reader(open("employees.csv", "rU"))

    # insert data into table
    stmt = "INSERT INTO employees(firstname, lastname) values (?, ?)"
    c.executemany(stmt, employees)


########################################################
#################### GIT COMMANDS ######################
########################################################
# book 2: pg 50?

### create virtual environment
# navigate to directory
# python -m venv env (or python3)

### activate virtual environment
# env\scripts\activate
# env\scripts\deactivate

## initialie local repo
# git init

##  Take a snapshot of the project in current state
# git add -A

## Add the project to your repo
# git commmit -m "init"

## add link to your remote repository
# git remote add origin https://github.com/<your-username>/real-python-test.git

## Push the local repo to Github
# git push origin master

## After local and remote git setup, use the following to continue PUSH as needed
# git add -A
# git commit -am 'msg: description of changes'
# git push origin master

# Every time part 2e
# $ git add .
# $ git commit -am "flask-hello-world" ## the "flask-hello-world" is the note I think
# $ git push origin master


####################
### Debugging #####
####################

#pg 107

# use pdb.set_trace()

# n : step forward one line
# p <variable name> : prints the current value of the provided variable
# l : displays the entire program along with where the current break point is
# q : exits the debugger and the program
# c : exits the debugger and the program continues to run
# b <line #> : adds a breakpoint at a specific line #
# args : displays values of arguments


#pg 115 Flask: Task Management Application


#pg 129 (bookmark)

######################
#### TESTING #########
######################

## Coverage (testing coverage reports)
## pip install coverage==4.2
## command line:
## coverage run test.py
## coverage report --omit=../env/'*'
## coverage html --omit=../env/'*'

## Nose (test discovery)
## pip install nose==1.3.7
## pip freeze > requirements.txt
## nosetests --with-coverage --cover-erase --cover-package=../project


## Hash Passwords ##
# pip install flask-bcrypt
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

#######################################################
### Heroku Deployments pg 254 (real python book 2)
#######################################################

# 1. Sign up for Heroku.
# 2. Log in and download the Heroku Toolbelt.
# 3. Once installed, open your terminal and run the following command: heroku login .
# You'll need to enter your email and password you used when you signed up for Heroku.

# 4. Navigate to your project and activate the virtual environment.
# 5. Install gunicorn: pip install gunicorn .
# 6. Heroku recognizes the dependencies needed through a requirements.txt file. Make
# sure to update you file: pip freeze > requirements.txt .

# 7. Create a Procfile. Open up a text editor and save the following text in it: web: python
# run.py . Then save the file in your application's root or main directory as Procfile (no
# extension). The word "web" indicates to Heroku that the application will be attached
# to HTTP once deployed to Heroku.

# THEN FOLLOW THESE STEPS

# reminder: push to github
# heroku create
# Heroku git:remote -a yourapp                     // your app = whatever heroku create returns
# heroku addons:create heroku-postgresql:dev       // add postgres DB. Used heroku UI instead

# heroku ps // make sure app is running
# heroku open // open app in browser
# heroku logs // check logs
# heroku run nosetests // run tests

#######################################################
# Automated Deployments pg 257 book 2
#######################################################

# pip install fabric3
# fabfile, fabfile.py // fabric is controlled by these files

# common commands
# run runs a command on a remote server
# local runs a local command
# put uploads a local file to the remote server
# cd changes the directory on the server side
# get downloads a file from the remote server
# prompt prompts a user with text and returns the user input

#### commit to github then push to heroku ###

## Prepare the files
# nosetests --with-coverage --cover-erase --cover-package=project // Test locally
# git add . // commit pt1 (not sure if I need to be in an active environment ot push, dont think for this setup I should)
# git commit -am "your message" // commit pt2
# git push origin master // push

## Deploy the files (Don't be in an active environment)
# git pull origin master // pull
# git push heroku master // push to heroku
# heroku run nosetests -v // test on heroku

#######################################################
## Create a blue print
#######################################################
# 1. create the view file in it's own sub folder
## - api_blueprint = Blueprint('api', __name__)
## - @api_blueprint.route('/api/v1/tasks/')
## - def api_tasks():
# 2. regiter the blueprint in project/__initi__.py
## - "from project.api.views import api_blueprint"
## - "app.register_blueprint(api_blueprint)"



######################################################
################### web2py
######################################################

# git clone https://github.com/web2py/web2py.git --recursive
# install virtual environment: python -m venv env
# activate virtual environment
# run "web2py.py" to launch server
# server is at localhost:port/welcome/default/index

# how to modify stuff
## edit the default controller with functions
## edit default/index.html with the view

# view py2manager tickets:
# http://127.0.0.1:8000/admin/default/errors/py2manager

#py2manager company/project/employee/notes tutorial, book 2 pg 403



#################
## SCRAPY
##################

# https://www.lfd.uci.edu/~gohlke/pythonlibs/ (38)
# $ pip install twisted (file above)
# $ pip install scrapy
# $ scrapy startproject hackernews
# $ cd hackernews
# $ scrapy genspider basic news.ycombinator.com
## modify items.py // define fields we want extracted
## modify basic.py // create spider
# scrapy shell http://news.ycombinator.com // start shell to test xpath
# save to DB: book 2 pg 449


#################
## DJANGO
##################
# pip install django
# django-admin.py startproject hello_world_project // setup new project
# python manage.py migrate
# python manage.py runserver 8080 // start server
# python manage.py startapp hello_world // create new app within project

''' 
Create a Project
1. Run python django-admin.py startproject <name_of_the_project> to create a new
Project. This will create the project in a new directory. Enter that new directory.
2. Migrate the database via python manage.py migrate .
Creating an App
1. Run python manage.py startapp <name_of_the_app> .
2. Add the name of the app to the INSTALLED_APPS tuple within settings.py file so that
Django knows that the new app exists.
3. Link the Application URLs to the main URLs within the Project's urls.py file.
4. Add the views to the Application's views.py file.
5. Add a urls.py file within the new application's directory to map the views to specific
URLs.
6. Create a "templates" directory, update the template path in the "settings.py" file, and
finally add any templates.
'''

# CREATE PROJECT
# update settings.py with name of new database
# $ python manage.py createsuperuser ## admin1234 | admin1234
# $ python manage.py startapp blog (create new app)
# update app/models.py
# update settings.py with name of app
# $ python manage.py makemigrations <appname> ## create migrations: tell django we want to update database tables based on models.py
# $ python manage.py migrate ## apply migrations: finally make the tables


## DJANGO orm
# python manage.py shell // start shell
# Post.objects.filter(id=1) // where post = class model name
# Post.objects.filter(id__gt==1)
# Post.objects.filter(title__contains='Charting')

# DJANGO testing
## update <app>/tests.py
## $ python manage.py test blog -v 2 // run tests

# DJANGO admin db updating
# update <app>/admin.py with...
## from django.contrib import admin
## from blog.models import Post
## admin.site.register(Post) // tells DJANGO which models to make available to admin


# DJANGO setup basic blog post website
## book2 pg 500
### create <project>/templates folder
### update settings.py to respect templates folder: 'DIRS': [os.path.join(BASE_DIR, 'templates')],
### update <app>/views.py with index function
### create new template file index.html
### Create <project>/<app>/urls.py and add route
### Update <project>/<project>/urls.py


# DJANGO tuples problem
'''
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^admin/', include(admin.site.urls)), // this doesn't work, must use path
    url(r'^blog/', include('blog.urls')),
]
'''

# DJANGO context problem
'''
c = Context({'latest_posts': latest_posts, }) // doesn't work anymore
c = ({'latest_posts': latest_posts, }) // remove "context" and pass as a dict
'''