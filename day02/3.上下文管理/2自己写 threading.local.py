#!/usr/bin/python3.5
# Author: xiaojie

import threading,time
from threading import get_ident

class Local(object):
    def __init__(self):
        self.storage = {}

    def __setitem__(self, key, value):
        ident = get_ident()
        if ident in self.storage:
            self.storage[ident][key] = value
        else:
            self.storage[ident] = {key:value}
    def __getattr__(self, key):
        ident = get_ident()
        return self.storage[ident][key]

obj=Local()


def task(arg):
    obj['value'] =arg
    time.sleep(0.5)
    print(obj.storage) #哪个线程先走完就输出


for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()