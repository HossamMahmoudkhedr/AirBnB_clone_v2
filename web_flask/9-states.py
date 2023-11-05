#!/usr/bin/python3
""" Script to start the flask web app """
from flask import Flask, render_template, Request
from functools import cmp_to_key
from models import storage
from models.state import State
from sys import path


path.append(path[0] + '/..')
app = Flask(__name__)


def namesort(entity1, entity2):
    if entity1.name > entity2.name:
        return 1
    elif entity1.name < entity2.name:
        return -1
    return 0


@app.teardown_appcontext
def app_teardown(self):
    """Remove the current SQLAlchemy session after each request"""
    print(self)
    storage.close()


@app.route("/states", strict_slashes=False)
def list_states():
    """Render the page displaying the list of states"""
    state_list = list(storage.all(State).values())
    state_list = sorted(state_list, key=cmp_to_key(namesort))
    return render_template("7-states_list.html", states=state_list)


@app.route("/states/<id>", strict_slashes=False)
def state_by_id(id):
    """Render the page displaying the list of states"""
    state_list = storage.all(State)
    found = None
    id = 'State.' + id

    if id in state_list.keys():
        found = state_list[id]
    state_list = state_list.values()
    print(f'id: {id}\n{found}')
    if found is None:
        return render_template("9-states.html", found=False, state=found)
    assert type(found) is State
    found.cities = sorted(found.cities, key=cmp_to_key(namesort))
    return render_template("9-states.html", found=True, state=found)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
