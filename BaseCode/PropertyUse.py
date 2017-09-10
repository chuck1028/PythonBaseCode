# -*- coding:utf-8 -*-
# Author: Jason Lee
class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setNum(self, newMoney):
        self.__money = newMoney

    money = property(getMoney, setNum)

m = Money()
print(m.money)
m.money = 100
print(m.money)