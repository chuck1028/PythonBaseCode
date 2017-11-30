class MyInt(int):
    def __pow__(self, value):
        return 'result: %s' % self * value

a = MyInt(2)

print(pow(a, 3))
