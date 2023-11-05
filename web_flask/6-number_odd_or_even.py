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


@app.route("/python", strict_slashes=False)
def python_default():
    """ python default route """
    return f'Python is cool'


@app.route("/python/<text>", strict_slashes=False)
def python_is(text):
    """ python path routing """
    return f'Python {escape(text)}'.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """ python path routing """
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ python path routing """
    return f'''<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: {n}</H1>
    </BODY>
</HTML>'''


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_even_odd(n):
    """ python path routing """
    return f'''<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: {n} is {'even' if n % 2 == 0 else 'odd'}</H1>
    </BODY>
</HTML>'''


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
