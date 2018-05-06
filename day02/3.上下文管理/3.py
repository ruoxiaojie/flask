#!/usr/bin/python3.5
# Author: xiaojie

import threading,time
from threading import get_ident


class Local(object):
    '''存数据'''
    def __init__(self):
        object.__setattr__(self,'__storage__',{})
    def __setitem__(self, key, value):
        ident = get_ident()
        try:
            self.storage[ident][key] = value
        except KeyError as e:
            self.__storage[ident] = {key:value}
    def __getattr__(self, key):
        ident = get_ident()
        try:
            return self.self.__storage__[ident][key]
        except Exception as e:
            return None


class LocalStack(object):
    def __init__(self):
        self._local = Local()
    def push(self,data):
        stack = self._local.stack
        if not stack:
            self._local.stack = []
        self._local.stack.append(data)


stack1 = LocalStack()
stack2 = LocalStack()

# stack1.push('x1')
# stack2.push('x2')

class RequestConrext(object):
    def __init__(self):
        self.request = '666'
        self.session = '999'

ctx = RequestConrext()
stack1.push(ctx)

class Flask(object):
    pass


stack2.push(Flask())