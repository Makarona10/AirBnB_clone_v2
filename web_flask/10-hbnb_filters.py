#!/usr/bin/python3

"""A script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def get_list():
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           amenities=amenities, states=states)


@app.teardown_appcontext
def teardown(e):
    """Ends up the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
