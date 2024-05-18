#!/usr/bin/python3

"""A script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_states(id=None):
    if id:
        states = storage.all("State").values()
        for state in states:
            if state.id == id:
                return render_template('9-states.html', states=states)
        return render_template("9-states.html")
    else:
        states = storage.all("State")
        return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown(e):
    """Ends up the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
