
# Team AKA Wolfgang: Kosta, Aaron, Andrew>
- SoftDev
- K12 -- Forms
- 2022-10-18
- Time Spent: 0.75 hours

## DISCO
- In the 'dictionary'-like object that contains the tuples of input form names and values, the key-value pairs are generated as they are passed in, not a priori
- methods parameter can specifiy what type of requests we make from the flask app, by default it's both GET and POST
- POST method is used to send data from the site to the server(send the data a user inputs into a field to the backend)
- GET method does what a POST but it also sends data to the site to publish/update it
- To force POST, we need to make a call to request.forms after a form has been filled out. In this case, if we specify the form to be "GET" then we will get an error, since only "POST" requests generate request.forms

### QCC
- What's the difference between GET and POST requests?
- How do we get a POST request to work?

'''
