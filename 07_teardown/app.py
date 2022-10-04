"""
Craig Chen, Aaron Gershkovich, Kosta Dubovskiy
SoftDev
07-app
-Apps and Flask-
2022-10-03
time spent: 20 minutes
"""

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
* Our program does not work for unanticipated reasons
* We host the app locally
* Upon the questioning and observation of other groups and through assumption of code we determined there should be a website
* The website should display the phrase "No hablo queso!" which is the return statement of the hello_world function
QCC:
-We are getting a circular error that we don't know how to fix
-We can't install or unistall the app to try again
-We seem to be the only ones with this issue

Questions:
0. Java init functions are similar, the __[]__ usually symbolizes something default
1. It means root directory often
2. To the app root directory, since we routed everything there
3. No hablo queso!
4. Probably on the website, since we routed the app there
5. We've seen similar stuff in Flutter and React/JS
...
INVESTIGATIVE APPROACH:
We initially read throught the given code, identifying that it was using an app
to create a local website on the computer, then we looked through the question
to see if it could shed any light on the content, which helped us understand the
subworkings of the program. Then we looked at a successful run of the program
to see if it did what we thought it would.
 *
'''
