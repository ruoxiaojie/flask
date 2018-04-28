#!/usr/bin/python3.5
# Author: xiaojie

def func(a1,a2,a3):
    return a1 + a2 + a3

# v = func(1,2,3)
# print(v)

import functools

f1 =functools.partial(func,1)
v = f1(2,3)
print(v)
