# -*- coding:utf-8 -*-
# Author: Jason Lee
class Test(object):
    pass

t = Test()

print('type(t)', type(t))

Test2 = type('Test2', (object,), {})

t2 = Test2()
print('type(t2)', type(t2))

def get_num(self):
    return self.num

Test3 = type('Test3', (object,), {'num' : 10, 'get_num': get_num})

t3 = Test3()
print('-->', t3.get_num())
