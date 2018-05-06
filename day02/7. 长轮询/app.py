from flask import Flask,render_template,request,session,redirect,jsonify
from uuid import uuid4
from queue import Queue,Empty
import json
app = Flask(__name__)
app.secret_key = "asdfasdfasdf"

UUUU = {
    '1':{'name':'start1','count':1},
    '2':{'name':'end2','count':1},
    '3':{'name':'yyl3','count':1},
}

# 为每个登录用户保存
# dfasdfadsfasdfadf: Queue()
USER_QUEUE_DICT = {

}

@app.before_request
def check_login():
    if request.path == '/login':
        return None
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        nid = str(uuid4())
        USER_QUEUE_DICT[nid] = Queue()
        session['user_info'] = {'nid':nid, 'user':user }
        return redirect('/index')


@app.route('/index')
def index():
    return render_template('index.html',user_list = UUUU)

@app.route('/query')
def query():
    """每个用户查询最新投票信息"""
    ret = {'status':True,'data':None}
    current_user_nid = session['user_info']['nid']
    queue = USER_QUEUE_DICT[current_user_nid]
    try:
        # {'uid':1, 'count':6}
        ret['data'] = queue.get(timeout=10)
    except Empty as e:
        ret['status'] = False
    # return jsonify(ret)
    return json.dumps(ret)


@app.route('/vote')
def vote():
    """
    用户投票
    :return:
    """
    uid = request.args.get('uid')
    old = UUUU[uid]['count']
    new = old + 1
    UUUU[uid]['count'] = new

    for q in USER_QUEUE_DICT.values():
        q.put({'uid':uid, 'count':new})

    return "投票成功"


if __name__ == '__main__':
    app.run(host='0.0.0.0',threaded=True)

