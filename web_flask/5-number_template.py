#!/usr/bin/python3
"""This script serves a Flask Web Application with 3 routes"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    route should match both trailing slash and no trailing slash'/' \
    - returns static content
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display static content in new route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Replace text in c route"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Replace text in python route"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display number only if it's an integer"""
    try:
        if not isinstance(n, int):
            return None
        else:
            return "{} is a number".format(n)
    except TypeError:
        return None


@app.route('/number/<int:n>', defaults={'n': None}, strict_slashes=False)
@app.route('/number_template/<int:n>', strict_slashes=False)
def display_page_number(n):
    """Render number template"""
    try:
        if not isinstance(n, int):
            return None
        else:
            return render_template('5-number.html', n=n)
    except TypeError:
        return None


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
