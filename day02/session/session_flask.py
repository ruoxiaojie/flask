#!/usr/bin/python3.5
# Author: xiaojie

from flask import Flask,session
from flask.ext.session import Session
from redis import Redis

app = Flask(__name__)


#将session保存到redis
app.secret_key = "dfghfghjk"
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host='192.168.1.1',port='6379')
Session(app)

@app.route('/login',methods=['GET','POST'])
def login():
    session['user_info'] = 'xxxxx'
    return 'login.html'

if __name__ == '__main__':

    app.run()