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
c = MyClass()
#c.test()
t = TestClass1()
print(t._meta)
