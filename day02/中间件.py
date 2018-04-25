#!/usr/bin/python3.5
# Author: xiaojie

from flask import Flask
app = Flask(__name__)

@app.route('/index',methods=['GET']) #多路由使用同一装饰器得加上endpoint endpoint='n2'
def index():
    return 'index.html'


class Middleware(object):
    def __init__(self,old_wsgi_app):
        self.old_wsgi_app = old_wsgi_app
    def __call__(self, *args, **kwargs):
        #还没有request  不能做请求相关操作
        resonse = self.old_wsgi_app(*args, **kwargs)
        return resonse

if __name__ == '__main__':
    #执行app 先执行__call   改写__call__
    app.wsgi_app = Middleware(app.wsgi_app)
    app.run()
