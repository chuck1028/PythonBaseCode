class MyMetaClass(type):
    def __new__(cls, *args, **kwargs):
        class_name = args[0]
        bases = args[1]
        attrs = args[2]
        # print(class_name)
        # print(bases)
        print(attrs)
        # print(kwargs)

        # print(dir(attrs))
        new_attrs = []
        for k, v in attrs.items():
            if not k.startswith('__'):
                new_attrs.append((k.upper(), v))
                continue
            new_attrs.append((k, v))

        new_attrs = dict(new_attrs)

        args = (class_name, bases, new_attrs)

        return super().__new__(cls, *args, **kwargs)


class Person(object, metaclass=MyMetaClass):
    # name = 'jason'

    def __init__(self, name):
        self.name = name

    def get_person_name(self):
        return self.name


def test():
    p = Person('jason')
    print(p.GET_PERSON_NAME())


class MyMetaClass1(type):
    def __new__(cls, *args, **kwargs):
        class_name = args[0]
        bases = args[1]
        attrs = args[2]
        print(class_name)
        print(bases)
        print(attrs)
        # print(kwargs)

        print(attrs['Meta'].name)

        return super().__new__(cls, *args, **kwargs)


class TestMeta(object, metaclass=MyMetaClass1):
    class Meta:
        name = 'jason'


def test1():
    t = TestMeta()


if __name__ == '__main__':
    # test()
    test1()
