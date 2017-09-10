# -*- coding:utf-8 -*-
# Author: Jason Lee
class Test(object):
    def __init__(self):
        # self.num = 100
        self.__num = 100

    def setNum(self, newNum):
        self.__num = newNum

    def getNum(self):
        return self.__num

t = Test()
# t.num = 200
# print(t.num)
# print(t._Test__num)
print(t.getNum())