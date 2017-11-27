# -*- coding:utf-8 -*-
# Author: Jason Lee

class RevealAccess(object):
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print('Retrieving:', self.name)
        return self.val

    def __set__(self, instance, value):
        print('Updating:', self.name)
        self.val = value

class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5

m = MyClass()
print(m.x)

m.x = 20
print(m.x)