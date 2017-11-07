#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-

from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/login',methods=['GET','POST'])
def login():
    print(request.method)
    return render_template('login.html')

if __name__ == '__main__':
    app.run()