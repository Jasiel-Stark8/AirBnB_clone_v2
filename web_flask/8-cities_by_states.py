#!/usr/bin/python3
"""This script starts a Flask Web Application"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """Render HTML template with all available states and their cities from database"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(self):
    """Terminate current Database Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
