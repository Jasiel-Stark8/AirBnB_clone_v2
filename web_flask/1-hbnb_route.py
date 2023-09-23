#!/usr/bin/python3
"""This script serves a Flask Web Application with 2 routes"""

from flask import Flask

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
