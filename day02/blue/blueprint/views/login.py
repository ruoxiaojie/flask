#!/usr/bin/python3.5
# Author: xiaojie

from flask import Blueprint

bc = Blueprint('bc',__name__)

@bc.route('/index')
def index():
    return 'index'