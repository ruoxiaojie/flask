#!/usr/bin/python3.5
# Author: xiaojie
from flask import *

app = Flask(__name__)

@app.route('/login')
def login():
    pass

@app.route('/index')
def index():
    pass


@app.route('/host')
def host():
    pass


if __name__ == '__main__':
    app.run()