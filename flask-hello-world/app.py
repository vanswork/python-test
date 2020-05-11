# import Flak 
from flask import Flask

# create application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use the decorator pattern to
# link the view function to a URL
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!!!!!!13"

# dynamic route
@app.route ("/test/<search_query>")
def searcch(search_query):
	return search_query

@app.route("/integer/<int:value>")
def int_type(value):
	print(value + 1)
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print(value + 1)
	return "correct"

@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return "correct"

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael" : 
		return "Hello, {}".format(name)
		return "Not Found!", 404


# start the development server using the run() method
if __name__ == "__main__":
	app.run()