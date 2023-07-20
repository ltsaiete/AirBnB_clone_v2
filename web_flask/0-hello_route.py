#!/usr/bin/python3
"""
This is a simple module that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello HBNB!'
