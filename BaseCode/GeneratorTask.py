# -*- coding:utf-8 -*-
# Author: Jason Lee
import time

def task1():
    while True:
        print('----task1---')
        yield None

def task2():
    while True:
        print('----task2---')
        yield None

t1 = task1()
t2 = task2()

while True:
    t1.__next__()
    t2.__next__()
    time.sleep(2)