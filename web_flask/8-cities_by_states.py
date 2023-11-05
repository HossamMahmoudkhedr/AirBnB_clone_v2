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


@app.route("/cities_by_states", strict_slashes=False)
def list_cities_by_state():
    """Render the page displaying the list of states"""
    state_list = list(storage.all(State).values())

    def namesort(entity1, entity2):
        if entity1.name > entity2.name:
            return 1
        elif entity1.name < entity2.name:
            return -1
        return 0
    state_list = sorted(state_list, key=cmp_to_key(namesort))
    for state in state_list:
        assert type(state) is State
        state.cities = sorted(state.cities, key=cmp_to_key(namesort))
    return render_template("8-cities_by_states.html", states=state_list)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
