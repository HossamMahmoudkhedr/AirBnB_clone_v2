#!/usr/bin/python3
""" Script to start the flask web app """
from flask import Flask, render_template, Request
from functools import cmp_to_key
from models import storage
from models.state import State
from sys import path


path.append(path[0] + '/..')
app = Flask(__name__)


@app.teardown_appcontext
def app_teardown(self):
    """Remove the current SQLAlchemy session after each request"""
    print(self)
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    """Render the page displaying the list of states"""
    state_list = storage.all(State).values()

    def namesort(entity1, entity2):
        if entity1.name > entity2.name:
            return 1
        elif entity1.name < entity2.name:
            return -1
        return 0
    state_list = sorted(state_list, key=cmp_to_key(namesort))
    return render_template("7-states_list.html", states=state_list)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
