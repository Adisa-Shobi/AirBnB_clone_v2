#!/usr/bin/python3
'''
Script runs flask web application listening on 0.0.0.0
and port 5000
'''
from flask import Flask, render_template
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


@app.route('/number/<int:n>')
def number_route(n):
    '''Route returns parameter only if it is an integer
    '''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''Render a template if an integer parameter is supplied
    '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''Render a template if an integer parameter is supplied
    telling either odd or even
    '''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
