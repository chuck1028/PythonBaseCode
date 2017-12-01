# -*- coding:utf-8 -*-
# Author: Jason Lee

class ContextManager(object):
    def __init__(self):
        self.entered = False

    def __enter__(self):
        self.entered = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.entered = False