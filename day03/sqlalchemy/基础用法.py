#!/usr/bin/python3.5
# Author: xiaojie




import sqlalchemy
#依赖pymysql 去连db 本身不能连
#sqlalchemy 不能修改表 #第三方组件

import time
import threading
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

engine = create_engine(
    "mysql+pymysql://all:123456@192.168.100.129:3306/nginx?charset=utf8",
    max_overflow=2,  # 超过连接池大小外最多创建的连接
    pool_size=2,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)



def task(arg):
    conn = engine.raw_connection()
    cursor = conn.cursor()
    # cursor.execute("select * from USER;",[])
    cursor.execute("select * from user;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    print(result)


for i in range(5):
    t = threading.Thread(target=task, args=(i,))
    t.start()