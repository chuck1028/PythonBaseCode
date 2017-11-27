# -*- coding:utf-8 -*-
# Author: Jason Lee

class DistinctError(ValueError):
    pass

class DistinctDict(dict):
    def __setitem__(self, key, value):
        if value in self.values():
            raise DistinctError('this value already exists...')
        super().__setitem__(key, value)


m = DistinctDict()
m['k'] = 'v'
m['kk'] = 'vv'