'''
https://flask.palletsprojects.com/en/2.2.x/installation/#virtual-environments
https://flask.palletsprojects.com/en/2.2.x/quickstart/
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def hello_test():
    return render_template("index.html")