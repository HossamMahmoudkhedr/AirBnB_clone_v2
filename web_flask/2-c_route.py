#!/usr/bin/python3
""" Module for an simple routing App """
from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ returns hello hbnb """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ returns hbnb """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    """ c path routing """
    return f'C {escape(text)}'.replace('_', ' ')


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
