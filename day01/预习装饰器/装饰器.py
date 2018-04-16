#!/usr/bin/python3.6
# Author: xiaojie


def wapper(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner


#(立即执行wapper函数，并将下面装饰的函数当成参数传递#
#将wapper函数返回值获取 在index赋值# )
#inner函数内部调用了原函数
@wapper
def index():
    print('函数')

index()