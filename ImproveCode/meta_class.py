# -*- coding:utf-8 -*-
# Author: Jason Lee


class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        # print(name)
        # print(bases)
        # print(attrs)
        if hasattr(attrs, 'Meta'):
            cls._meta = attrs['Meta']
        return super().__new__(cls, name, bases, attrs)


class CommonClass(object, metaclass=MetaClass):
    class Meta:
        name = 'Jason'

# c = CommonClass()

# print(c._meta)
# print(CommonClass.Meta)


class ObjectCreator(object):
    pass


def echo(o):
    print(o)


def create_class(name):
    if name == 'Foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar


def create_class_by_type(name):
    new_class = type(name, (object,), {name.lower(): 'TT'})

    return new_class


def test1():
    my_object = ObjectCreator()
    echo(my_object)

    print(hasattr(my_object, 'new_attribute'))
    my_object.new_attribute = 'foo'
    print(hasattr(my_object, 'new_attribute'))
    print(my_object.new_attribute)

    MyClass = create_class('Foo')
    echo(MyClass())


# type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
def test2():
    my_class = create_class_by_type('Foo')
    echo(my_class())
    # print(dir(my_class))
    # print(dir(int))
    print(my_class.__class__)


# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """返回一个类对象，将属性都转为大写形式"""
    # 选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))

    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)


# __metaclass__ = upper_attr  # 这会作用到这个模块中的所有类


class Foo(object, metaclass=upper_attr):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'


def test3():
    print(hasattr(Foo, 'bar'))    # 输出: False

    print(hasattr(Foo, 'BAR'))    # 输出:True

    f = Foo()
    print(f.BAR)    # 输出:'bip'


# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type(future_class_name, future_class_parents, uppercase_attr)


class UpperAttrMetaclass(type):
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        # 复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        return type.__new__(upperattr_metaclass, future_class_name, future_class_parents, uppercase_attr)


class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(cls, name, bases, uppercase_attr)


class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)


if __name__ == '__main__':
    # test1()
    # test2()
    test3()
