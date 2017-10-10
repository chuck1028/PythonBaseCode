def with_metaclass(meta, *bases):
    print('--- with_metaclass ---')
    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            print('--- AAA ---')
            return meta(name, bases, d)
    print('--- BBB ---')
    return type.__new__(metaclass, 'temporary_class', (), {})

class BaseClass(type):
    def __new__(cls, name, bases, attrs):
        new_class = super(BaseClass, cls).__new__(cls, name, bases, attrs)
        opts = getattr(new_class, 'Meta', None)
        print('--- attrs --->', attrs)
        print('--- Meta --->', opts)

new_class = with_metaclass(BaseClass)

class OuterClass(new_class):
    date = '2017-10-10'
    class Meta:
        name = 'Jason'

#o = OuterClass()
    
