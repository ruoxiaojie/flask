#!/usr/bin/python3.5
# Author: xiaojie

import threading




obj=threading.local()
#threading.local 可以为每个线程 创建独立的空间  存放数据

def task(arg):
    global obj
    obj.value = arg
    print(obj.value)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()