# -*- coding:utf-8 -*-
# Author: Jason Lee

import types

def test(self):
    print('--- test ---')

class Method(object):
    @classmethod
    def class_method(cls):
        print('--- class method ---')

    @staticmethod
    def static_method():
        print('--- static method ---')

    def object_method(self):
        print('--- object_method ---')

m = Method()
#给对象动态添加方法
m.test = types.MethodType(test, m)
m.test()
# Method.static_method()
# m.static_method()

# Method.class_method()
# m.class_method()