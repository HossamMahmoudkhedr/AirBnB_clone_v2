#!/usr/bin/python3
""" Script to start the flask web app """
from flask import Flask, render_template, Request
from functools import cmp_to_key
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.user import User
from sys import path


path.append(path[0] + '/..')
app = Flask(__name__)


def namesort(entity1, entity2):
    """sort by name attribute"""
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


@app.route("/hbnb", strict_slashes=False)
def render_complete_template():
    """Render the page displaying the list of states"""
    state_list = storage.all(State).values()
    amenity_list = storage.all(Amenity).values()
    place_list = storage.all(Place).values()
    user_list = storage.all(User).values()
    for state in state_list:
        state.cities = sorted(state.cities, key=cmp_to_key(namesort))
    for place in place_list:
        assert type(place) is Place
        for user in user_list:
            assert type(user) is User
            if user.id == place.user_id:
                place.user = f'{user.first_name} {user.last_name}'
    return render_template("100-hbnb.html",
                           states=state_list,
                           amenities=amenity_list,
                           places=place_list)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
