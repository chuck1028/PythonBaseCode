# -*- coding:utf-8 -*-
# Author: Jason Lee
def w1(f):
    def inner():
        print('---w1---')
        f()
    return inner
@w1
def f1():
    print('---f1---')

f1()