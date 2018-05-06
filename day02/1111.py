#!/usr/bin/python3.5
# Author: xiaojie

user_status = False

def auth(user_status):
    def inner(func):
        def wrapper(*args, **kwargs):
            while True:
                if user_status:
                    return func(*args, **kwargs)
                else:

                    user_name = input("input your name:").strip()
                    user_password = input('input your password').strip()
                    if user_name == '':
                        continue
                    if user_name == 'alex' and user_password == '123':
                        print('登录成功！')
                        user_status = True
                        return func(*args, **kwargs)
                    else:
                        print('用户名或密码错误！')
                        break
        return wrapper
    return inner


import time


@auth(user_status)
def foo():
    time.sleep(1)
    print('hello')


