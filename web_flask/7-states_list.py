#!/usr/bin/python3
'''
Script runs flask web application listening on 0.0.0.0
and port 5000
'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''
    Default route for mimimal flask application
    '''
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
