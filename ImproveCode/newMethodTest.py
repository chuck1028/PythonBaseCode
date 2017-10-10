class NewClass(object):
    def __init__(self):
        print('__init__')

    def __new__(cls, *args, **kwargs):
        print('__new__')
        print(cls, '-', args, '-', kwargs)
        return super().__new__(cls, *args, **kwargs)

n = NewClass()
