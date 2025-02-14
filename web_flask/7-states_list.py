#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ state"""
    state = storage.all(State).values()
    return render_template('7-states_list.html', data=state)


@app.teardown_appcontext
def teardown(execption):
    """Inicializacion funtions"""
    return storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
