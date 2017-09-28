# -*- coding:utf-8 -*-
# Author: Jason Lee
args_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

def func(**kwargs):
    print(kwargs)

func(**args_dict)
func(d=4, e=5, f=6)