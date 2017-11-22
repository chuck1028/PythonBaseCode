# -*- coding:utf-8 -*-
# Author: Jason Lee

class CountDown(object):
    def __init__(self, step):
        self.step = step

    def __next__(self):
        if self.step <= 0:
            raise StopIteration

        self.step -= 1
        return self.step

    def __iter__(self):
        return self

# for element in CountDown(4):
#     print(element)

def fibonacci(num):
    a, b = 0, 1
    count = 0
    while count <= num:
        yield b
        a, b = b, a + b
        count += 1

fib = fibonacci(100)
for i in fib:
    print(i)
