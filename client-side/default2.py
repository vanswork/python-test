# Submitting to a web form
import requests

url = 'http://httpbin.org/post'
data = {'fname': 'Michael', 'lname': 'Herman', 'blah': 'something'}


# submit post request
r = requests.post(url, data=data)


# display the response to screen
print(r.content)