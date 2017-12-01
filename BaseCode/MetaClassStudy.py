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

class MetaClass(type):
    def __new__(cls, name, bases, namespace):
        print('__new__:', name, bases, namespace)
        return super().__new__(cls, name, bases, namespace)

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        print('__prepare__:', name, bases, kwargs)
        return super().__prepare__(cls, name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        print('__init__:', name, bases, namespace, kwargs)
        super().__init__(name, bases, namespace)

    def __call__(self, *args, **kwargs):
        print('__call__:', args, kwargs)
        return super().__call__(*args, **kwargs)


class Klass(object, metaclass=MetaClass, extra='value'):
    pass
