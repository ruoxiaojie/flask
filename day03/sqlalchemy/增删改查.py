#!/usr/bin/python3.5
# Author: xiaojie






from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from orm_createtable import Users

engine = create_engine("mysql+pymysql://all:123456@192.168.100.129:3306/nginx?charset=utf8",
                       max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)
session = Session()

###添加数据
# obj=Users(name="xiao")
# session.add(obj)
# session.commit()
# session.close()
#查询数据
# result=session.query(Users).all()
# for row in result:print(row.id,row.name)

# result=session.query(Users).filter(Users.id > 1)
# for row in result:print(row.id,row.name)

#删除数据
# session.query(Users).filter(Users.id > 1).delete()
# session.commit()
# session.close()
#
#修改数据
# session.query(Users).filter(Users.id > 0).update({'name':'super'})
# session.commit()
# session.close()





