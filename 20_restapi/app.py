# unknown: Aaron Gershkovich, Maya Nelson, Julia Lee
# SoftDev
# K20: A RESTful Journey Skyward
# 2022-11-23
# time spent: 0.75 hrs

import requests
from flask import Flask
from flask import render_template



app = Flask(__name__) #create instance of class Flask

with open("key_nasa.txt") as APIKey:
    key = APIKey.read()

@app.route("/")       #assign fxn to route
def hello_world():
    resp = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + key)
    resp = resp.json()

    exp = resp.get("explanation")
    url = resp.get("hdurl")

    return render_template("main.html", exp=exp, url=url)

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
