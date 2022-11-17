#!/usr/bin/python3
'''
Script runs flask web application listening on 0.0.0.0
and port 5000
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    '''
    Default route for mimimal flask application
    '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    Default hbnb route for flask application
    '''
    return "HBNB"


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
