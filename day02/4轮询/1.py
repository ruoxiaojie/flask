#!/usr/bin/python3.5
# Author: xiaojie

from flask import Flask,render_template,request,session,redirect
from uuid import uuid4
from queue import Queue

app = Flask(__name__)

UUU = {
    '1':{'name':'xiaojie','count':1},
    '2':{'name':'cool','count':1},
}
USER_QUERY_DICT = {

}

@app.before_request
def check_login():
    if request.path == '/login':
        return None
    userinfo = session.get('userinfo')
    if not userinfo:
        redirect('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        nid = str(uuid4())
        USER_QUERY_DICT[nid] = Queue()
        session['userinfo'] = {'nid':nid, 'user':user}
        return redirect('index')

@app.route('/index')
def index():
    return render_template('index.html',userlist=UUU)

@app.route('/query')
def query():
    #查询最新投票信息
    current_user_nid = session['userinfo']
    queue = USER_QUERY_DICT[current_user_nid]
    try:
        info = queue.get(timeout=10)
    except Empty as e:
        info = None

@app.route('/vote')
def vote():
    pass




if __name__ == '__main__':

    app.run()