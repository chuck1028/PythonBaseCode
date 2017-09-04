class MyClass(object):
    def test(self):
        print(self._meta)
        print(self._meta.name)

class TestClass(MyClass):
    class meta:
        name = 'jason'

c = MyClass()
c.test()
