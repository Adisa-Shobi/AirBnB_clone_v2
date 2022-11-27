#!/usr/bin/python3
'''
Script runs flask web application listening on 0.0.0.0
and port 5000
'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def home():
    '''
    Default route for mimimal flask application
    '''
    states = storage.all(State)
    amenities = storage.all(Amenity)
    print(amenities)
    return render_template("10-hbnb_filters.html",
                           states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    '''Tears down the current sqlalchemy session after each request
    '''
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
