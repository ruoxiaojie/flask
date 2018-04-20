#!/usr/bin/python3.5
# Author: xiaojie

from flask import Flask,render_template,request,session,redirect
from flask_admin import Admin


app = Flask(__name__,template_folder='templates')

from flask import Flask

from flask_admin import Admin, BaseView, expose


from flask import Flask

from flask_admin import Admin, BaseView, expose

app = Flask(__name__)

admin = Admin(app,name=u'后台管理系统')

app.run()

