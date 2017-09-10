# -*- coding:utf-8 -*-
# Author: Jason Lee
class Money(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('Error: The value must be an integer.')

m =Money()
print(m.money)
m.money = 100
print(m.money)