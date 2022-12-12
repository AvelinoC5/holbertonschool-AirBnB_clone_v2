#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """home page"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """two page"""
    return "HBNB"


@app.route('/c/<text>')
def C(text):
    """ three page"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    """ four page"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def number(n):
    """ five page"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def templete(n):
    """ six page"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def templete_two(n):
    """ siven page"""

    if (n % 2) == 0:
        n = '{} is even'.format(n)
        return render_template('6-number_odd_or_even.html', number=n)

    else:
        n = '{} is odd'.format(n)
        return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
