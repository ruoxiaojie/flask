#!/usr/bin/python3.5
# Author: xiaojie

from flask import Flask,render_template,request,session,redirect

app = Flask(__name__,template_folder='templates')


def index():
    return r'index.html'


if __name__ == '__main__':
    app.run()