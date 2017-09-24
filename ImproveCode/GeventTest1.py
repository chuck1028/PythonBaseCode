# -*- coding:utf-8 -*-
# Author: Jason Lee
import gevent
import time

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(1)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

#等待协程执行完毕
g1.join()
g2.join()
g3.join()