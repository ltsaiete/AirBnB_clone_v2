#!/usr/bin/python3
"""
This is a simple module that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

app.config['RESTFUL_URL_PREFIX'] = False


@app.route('/')
def index():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    return f'C {escape(text).replace("_", " ")}'


@app.route('/python/')
@app.route('/python/<text>')
def py_text(text='is cool'):
    return f'Python {escape(text).replace("_", " ")}'


@app.route('/number/<int:n>')
def show_number(n):
    return f'{escape(n)} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<n>')
def number_odd_or_even(n):
    even = 'even'
    if int(n) % 2 != 0:
        even = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, even=even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
