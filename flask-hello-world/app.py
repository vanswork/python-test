# import Flak 
from flask import Flask

# create application object
app = Flask(__name__)

# use the decorator pattern to
# link the view function to a URL
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
	return "Hello, World3!"


# start the development server using the run() method
if __name__ == "__main__":
	app.run()