#!/usr/bin/python3.5
# Author: xiaojie

class Foo(object):

    def __init__(self,age,name):
        self.age = age
        self.name =name

class Bar(object):
    def __init__(self,counter):
        self.counter = counter
        self.obj = Foo('19','ande')
b1 = Bar(1)

print(b1.obj.name)



