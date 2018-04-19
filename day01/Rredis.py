#!/usr/bin/python3.5
# Author: xiaojie

import redis


redis_config ={
    "host":'192.168.200.140',
    "port":'6379',
    "db":'0'
}

pool = redis.ConnectionPool(**redis_config)
r = redis.Redis(connection_pool=pool)

for i in range(100,100000):
    a="k" + str(i)
    r.set(a,i)
print('wanbi')