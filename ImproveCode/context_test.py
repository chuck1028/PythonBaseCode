# -*- coding:utf-8 -*-
# Author: Jason Lee

class ContextIllustration(object):
    def __enter__(self):
        print('---enter---')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('---exit---')

        if exc_type is None:
            print('---no error---')
        else:
            print('---error: %s---' % exc_val)