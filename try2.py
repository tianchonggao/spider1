#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read()
    soup = BeautifulSoup(content,"lxml")
    for link in soup.find_all('img'):
        name=link.get('alt')
        if name:
            print(name)
    print('xxx')
    for link in soup.find_all('div'):
        name=link.get('alt')
        if name:
            print(name)




    #print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
