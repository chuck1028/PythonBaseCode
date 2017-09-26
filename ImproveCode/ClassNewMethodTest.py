class Person(object):
    def __init__(self, name, age):
        print('__init__ Methon')
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print('__new__ Method is invoking')
        print('type(cls): ', type(cls))
        print('cls name: ', cls.__name__)
        return super(Person, cls).__new__(cls)

p = Person('Jason', 26)
print(p.name)
print(p.age)
