#!/usr/bin/python3
"""This script serves a Flask Web Application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Page is served with or without '/' - returns static content"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display static content in new route"""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
