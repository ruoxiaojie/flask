#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__) #__name__ 模块名 可以改
#添加路由的第一种方式
'''
@app.route('/') #路由规则  装饰器 执行app返回一个函数
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
'''
'''
#添加路由的第二种方式
def index():
    return 'Index'

app.add_url_rule('/index',view_func=index)              #加路由

if __name__ == '__main__':
    app.run()
'''
'''
#添加路由的第三种方式
@app.route('/xiaojie/<int:nid>',methods=['GET'])
def hello_world(nid):
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
'''
