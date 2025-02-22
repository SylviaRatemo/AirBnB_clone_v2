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


@app.route('/python', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def piscool(text):
    return "Python %s" % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'%d is a number' % n


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
