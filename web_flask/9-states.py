#!/usr/bin/python3
"""This script starts a Flask Web Application"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page with the list of all State objects"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """Display a HTML page with the list of City objects linked to the State"""
    states = storage.all(State).values()
    state = next((state for state in states if state.id == id), None)
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
