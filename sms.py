#!/usr/bin/python
# -*- coding: utf-8 -*-
  
import urllib
import urllib2
import re

smsLoginUrl="http://ln.pro-group.com.cn:8888/logins.html"
testUrl="http://ln.pro-group.com.cn:8888/code.aspx"

#headers = {
#    'Accept':'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#    'Accept-Encoding':'gzip, deflate, sdch',
#    'Accept-Language':'zh-CN,zh;q=0.8',
#    'Cache-Control':'no-cache',
#    'Connection':'keep-alive',
#    'Host':'ln.pro-group.com.cn:8888',
#    'Pragma':'no-cache',
#    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'
#    }


#username="10690570000016"
#password="zbmf7878"

#postData = {   
#    '用户名':username, 
#    '密  码':password,
#    '验证码':''
#     }

#def login():
#    smspage = urllib2.urlopen(smsLoginUrl)
#    sendPostData(smsLoginUrl,postData,headers)

#def sendPostData(url,data,header):
#    request = urllib2.Request(url, data, header)
#    response = urllib2.urlopen(request)
#   print response


smspage = urllib2.urlopen(testUrl)
print smspage.read()  
    
