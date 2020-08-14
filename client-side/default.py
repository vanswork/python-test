# Retrieving a web page
import requests


# retrieve the web page
r = requests.get("http://www.python.org/")


# write the content to test_request.html
with open("test_requests.html", "wb") as code:
    code.write(r.content)


# print(r.content)