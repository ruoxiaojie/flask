#!/usr/bin/python3.5
# Author: xiaojie
from pymysql import connect
import pymysql

mysql_conf={
    "host":"192.168.100.129",
    "port":3306,
    "user":"all",
    "passwd":"123456",
    "db":"nginx"
}
#创建连接
conn = connect(**mysql_conf)

#创建游标
# cursor = conn.cursor() #元组
cursor = conn.cursor(pymysql.cursors.DictCursor) #字典

#执行sql 返回结果

row = cursor.execute("select * from user")
result = cursor.fetchall()

print(result)
#关闭游标连接
cursor.close()
conn.close()


