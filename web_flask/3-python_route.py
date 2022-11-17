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


@app.route('/c/<text>', strict_slashes=False)
def route_c(text):
    '''Route accepts parameter and returns manipulated version
    '''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def route_python(text="is cool"):
    '''Route accepts parameter and returns manipulated version
    preceded by Python
    '''
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
