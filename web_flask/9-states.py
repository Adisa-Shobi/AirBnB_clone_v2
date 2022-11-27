#!/usr/bin/python3
'''
Script runs flask web application listening on 0.0.0.0
and port 5000
'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    '''
    Default route for mimimal flask application
    '''
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    '''
    Default route for mimimal flask application
    '''
    states = storage.all(State)
    try:
        queried_state = states["State.{}".format(id)]
    except Exception:
        queried_state = ""
    return render_template("9-states.html", state=queried_state)


@app.teardown_appcontext
def teardown(exception):
    '''Tears down the current sqlalchemy session after each request
    '''
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
