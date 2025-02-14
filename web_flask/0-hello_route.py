#!/usr/bin/python3
"""This script serves a Flask Web Application"""

# Import Flask
from flask import Flask

# Initialize Flask app
app = Flask(__name__)


# Define route and server content
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Page is served with or without '/' - returns static content"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
