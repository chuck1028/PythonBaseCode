#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib2

response = urllib2.urlopen('http://www.baidu.com/')

html = response.read()

print html
