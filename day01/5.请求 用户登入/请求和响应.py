from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import make_response

app = Flask(__name__)


@app.route('/login.html', methods=['GET', "POST"])
def login():

    # 请求相关信息
    # request.method
    # request.args
    # request.form
    # request.values
    # request.cookies
    # request.headers
    # request.path
    # request.full_path
    # request.script_root
    # request.url
    # request.base_url
    # request.url_root
    # request.host_url
    # request.host
    # request.files
    # obj = request.files['the_file_name']
    # obj.save('/var/www/uploads/' + secure_filename(f.filename))

    # 响应相关信息
    # return "字符串"
    # return render_template('html模板路径',**{})
    # return redirect('/index.html')

    # response = make_response(render_template('index.html'))
    # response是flask.wrappers.Response类型
    # response.delete_cookie('key')
    # response.set_cookie('key', 'value')
    # response.headers['X-Something'] = 'A value'
    # return response


    return "内容"

if __name__ == '__main__':
    app.run()