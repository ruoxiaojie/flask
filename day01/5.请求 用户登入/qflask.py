#!/usr/bin/python3.5
# Author: xiaojie

from flask import Flask,render_template,request,session,redirect
import functools

app = Flask(__name__,template_folder='templates')
#template_folder='templates'默认
app.secret_key = "helloworld" #设置session


#用户请求  ==》 app.before_request 我 ==》app.after_request ==》用户

@app.before_request #请求前 无参数 无返回值  #最牛B的用户登入##
def bf():
    if request.path == "/login":
        return None
    user_info = session.get('user_info')
    if not user_info:
        return "用户未登入"


@app.after_request #请求后 有参数 有返回值
def af(response):
    print('af_request')
    return response


@app.route('/order',methods=['GET'])
def order():
    return 'order'

@app.route('/index',methods=['GET']) #多路由使用同一装饰器得加上endpoint endpoint='n2'
def index():
    return 'index'

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