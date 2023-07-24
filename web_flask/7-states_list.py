#!/usr/bin/python3
"""Flask app"""

from flask import Flask, render_template
from models import *
from models import State
app = Flask(__name__)


@app.teardown_appcontext
def closedb(foo):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
     states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
