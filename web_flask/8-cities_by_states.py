#!/usr/bin/python3
'''
Script runs flask web application listening on 0.0.0.0
and port 5000
'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''
    Default route for mimimal flask application
    '''
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    '''Tears down the current sqlalchemy session after each request
    '''
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
