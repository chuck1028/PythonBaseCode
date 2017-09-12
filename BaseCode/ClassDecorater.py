# -*- coding:utf-8 -*-
# Author: Jason Lee
class Test(object):
    def __init__(self, func):
        print('---init---')
        print('func name: %s' % func.__name__)
        self.__func = func

    def __call__(self):
        print('---call---')
        self.__func()

@Test
def test():
    print('---test---')
