#!/usr/bin/env python3
"""This script starts a Flask Web Application"""
# Import Flask
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Define routes and return static content
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
