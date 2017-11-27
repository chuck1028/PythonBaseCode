# -*- coding:utf-8 -*-
# Author: Jason Lee


class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        print(name)
        print(bases)
        print(attrs)
        if hasattr(attrs, 'Meta'):
            cls._meta = attrs['Meta']
        return super().__new__(cls, name, bases, attrs)

class CommonClass(object, metaclass=MetaClass):
    class Meta:
        name = 'Jason'

c = CommonClass()

# print(c._meta)
print(CommonClass.Meta)