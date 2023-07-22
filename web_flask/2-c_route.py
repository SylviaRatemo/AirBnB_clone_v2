#!/usr/bin/python3
"""Flask app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return f'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    return "C %s" % text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
