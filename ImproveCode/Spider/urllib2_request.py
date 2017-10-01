#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib2

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3368.400 QQBrowser/9.6.11974.400",
}

#urllib2.Request(url, data, headers)
request = urllib2.Request('http://www.baidu.com/', headers=headers)

response = urllib2.urlopen(request)

html = response.read()

print html

print response.getcode()
print response.geturl()
print response.info()

