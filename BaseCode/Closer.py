# -*- coding:utf-8 -*-
# Author: Jason Lee
def test(number):
    def test_in():
        print (number + 100)
    return test_in

# f = test(1)
# print(f)
# f()

def draw_line(a, b):
    def line(x):
        print(a * x + b)
    return line

line1 = draw_line(1, 1)
line2 = draw_line(2, 3)
line1(1)
line2(2)