#!/usr/bin/python3

"""A script that starts a Flask web application"""


from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """The homepage function"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb function"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def name(text):
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/number/<int:n>', strict_slashes=False)
def isInt(n):
    if isinstance(n, int):
        return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template2(n):
    if isinstance(n, int):
        nType = "even" if n % 2 == 0 else "odd"
        return render_template('6-number_odd_or_even.html',
                               number=n, type=nType)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
