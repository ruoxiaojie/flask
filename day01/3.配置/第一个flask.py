#!/usr/bin/python3.5
# Author: xiaojie

from flask import Flask,render_template,request,session,redirect

app = Flask(__name__,template_folder='templates')




app.config.from_object('settings.TestConfig')



@app.route('/index',methods=['GET'])

def index():
    return render_template('index.html')

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


if __name__ == '__main__':
    app.run()