#!/usr/bin/python3
"""
This is a simple module that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
