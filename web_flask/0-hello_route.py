#!/usr/bin/env python3
"""This script serves a Flask Web Application"""
# Import Flask
from flask import Flask

# Initialize Flask app
app = Flask(__name__)
app.url_map.strict_slashes = False


# Define routes and return static content
@app.route('/')
def hello_hbnb():
    return "Hello HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
