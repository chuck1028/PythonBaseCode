# -*- coding:utf-8 -*-
# Author: Jason Lee
import time
import itertools

def squares(cursor=1):
    response = None
    while True:
        if response:
            response = yield response ** 2
            continue

        response = yield cursor ** 2
        cursor += 1


def task1():
    while True:
        print('----task1---')
        yield None

def task2():
    while True:
        print('----task2---')
        yield None

# t1 = task1()
# t2 = task2()
#
# while True:
#     t1.__next__()
#     t2.__next__()
#     time.sleep(2)

def gen1():
    yield 'foo'
    yield 'bar'


def gen2():
    yield 'spam'
    yield 'eggs'


def full_gen1():
    for word in gen1():
        yield word

    for word in gen2():
        yield word


def full_gen2():
    for word in itertools.chain(gen1(), gen2()):
        yield word


def full_gen3():
    yield from gen1()
    yield from gen2()

for i in full_gen3():
    print('--->', i)

