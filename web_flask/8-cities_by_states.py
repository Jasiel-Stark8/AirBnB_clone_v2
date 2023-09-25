#!/usr/bin/python3
"""This script Displays citeis by States"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """Terminate current Database Session"""
    storage.close()


@app.route('/cities_by_states')
def display_cities():
    """This displays cities"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    states = sorted(states, key=lambda state: state.name)
    cities = sorted(cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
