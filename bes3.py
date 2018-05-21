# -*- coding:utf-8 -*-
 
import urllib
import urllib2
import cookielib
import re
 
#山东大学绩点运算
class SDU:
 
    def __init__(self):
        self.loginUrl = 'http://hnbes3.ihep.ac.cn/statistics.php'
        self.cookies = cookielib.CookieJar()
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }  
        self.postdata = urllib.urlencode({
            'stuid':'huyu',
            'pwd':'huyu1111'
         })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
 
    def getPage(self):
        request  = urllib2.Request(
            url = self.loginUrl,
            data = self.postdata,
            headers = self.headers)
        result = self.opener.open(request)
        #打印登录内容
        print result.read().decode('gbk')
 
 
sdu = SDU()
sdu.getPage()
