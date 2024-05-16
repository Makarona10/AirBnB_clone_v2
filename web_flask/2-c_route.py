#!/usr/bin/python3

"""A script that starts a Flask web application"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """The homepage function"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """The homepage function"""
    return "HBNB"


@app.route('/c/<text>')
def name(text):
    return f"C {escape(text.replace('_', ' '))}!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
