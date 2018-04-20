#!/usr/bin/python3.5
# Author: xiaojie

from flask import Flask,render_template,request,session,redirect
import functools

app = Flask(__name__,template_folder='templates')
#template_folder='templates'默认
app.secret_key = "helloworld" #设置session


@app.route('/index',methods=['GET']) #多路由使用同一装饰器得加上endpoint endpoint='n2'
def index():
    context = {
        'k1':'v1',
        'k2': [11,22,33],
        'k3':{'kk2':'vv1'}
    }
    return render_template('index.html',**context)


if __name__ == '__main__':
    app.run()