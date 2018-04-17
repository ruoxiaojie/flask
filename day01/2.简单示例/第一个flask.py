#!/usr/bin/python3.5
# Author: xiaojie

from flask import Flask,render_template,request,session,redirect
import functools

app = Flask(__name__,template_folder='templates')
#template_folder='templates'默认
app.secret_key = "helloworld" #设置session



def auth(func):
    '''
    用户登入session装饰器
    :param func:
    :return:
    '''
    @functools.wraps(func) #多装饰器需要添加endpoint endpoint
    def inner(*args,**kwargs):
        user_info = session.get('user_info')
        if not user_info:
            return redirect('/login')
        return func(*args,**kwargs)
    return inner



@app.route('/index',methods=['GET']) #多路由使用同一装饰器得加上endpoint endpoint='n2'
@auth
def index():
    return render_template('index.html')

@app.route('/order',methods=['GET'])
@auth
def order():

    return 'order'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'xiaojie' and pwd == '123':
            session['user_info'] = user
            return render_template('index.html')
        return render_template('login.html',msg = "用户名密码错误")

@app.route('/logout',methods=['GET'])
def logout():
    del session['user_info']
    return redirect('/login')


if __name__ == '__main__':
    app.run()