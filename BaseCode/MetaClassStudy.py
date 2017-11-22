class MyClass(object):
    def test(self):
        print(self._meta)
        print(self._meta.name)

class TestClass(MyClass):
    class Meta:
        name = 'jason'

class TestClass1(object):
    class Meta:
        name = 'jason'
# c = MyClass()
#c.test()
# t = TestClass1()
# print(t._meta)

class MyMetaClass(type):
    def __new__(cls, *args, **kwargs):
        print('args--->', args)
        print('kwargs--->', kwargs)
        return super().__new__(cls,*args, **kwargs)


class MySubClass(metaclass=MyMetaClass):
    def __init__(self):
        print('__init__')


m = MySubClass()



