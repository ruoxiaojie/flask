#!/usr/bin/python3.5


class Teacher:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def tell_info(self):
        print('姓名:{0},年龄:{1}'.format(self.__name,self.__age))
    def set_info(self,name,age):
        if not isinstance(name,str):
            raise TypeError('姓名必须是字符串类型')
        if not isinstance(age,int):
            raise TypeError('年龄必须是整型')
        self.__name=name
        self.__age=age

p=Teacher('xiaojie',18)


t.set_info('xiaojie',19)
t.tell_info()

#隐藏，并对外提供接口，接口附加类型检查逻辑