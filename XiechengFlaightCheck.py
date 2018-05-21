# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 22:11:50 2018

@author: HuYu
"""

#import urllib2
import urllib.request
import json
from lxml import etree
import random
import time
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

def get_that():
    
    url='http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=HRB&ACity1=SHA&SearchType=S&DDate1=2016-05-13&IsNearAirportRecommond=0&rk=5.189667156909168071745&CK=89D3A4A3A5F8A7F7E48ACDD1F451127A&r=0.1440474125154478474718'

    response=urllib.request.urlopen(url).read()
    print(response)
    
def get_json():
    url='https://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=SHA&ACity1=HRB&SearchType=S&DDate1=2018-04-26&IsNearAirportRecommond=0&LogToken=d7810f125c1644839993613d84dc9a86&rk=8.287372302409393052146&CK=75242CF5AA0FD7913EEEBAB938DFC358&r=0.2844713440560481963012'
    headers={'Host':"flights.ctrip.com",'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",'Referer':"http://flights.ctrip.com/booking/hrb-sha-day-1.html?ddate1=2016-05-13"}
    req=urllib.request.Request(url,headers=headers)
    res=urllib.request.urlopen(req).read().decode("gb2312")
    #print(content)
    dict_content=json.loads(res)
    print(len(dict_content['fis']))
    Comp = dict_content['als']
    print(Comp)
    for jsoni in dict_content['fis']:
        com = jsoni['alc']
        comp = Comp[com]
        start = jsoni['dpbn']##起飞时地址
        stop = jsoni['apbn']##降落地址
        startDate = jsoni['dt']##起飞时间
        stopDate = jsoni['at']##降落时间
        timeStart = time.strptime(startDate,'%Y-%m-%d %H:%M:%S')
        timeStop = time.strptime(stopDate, '%Y-%m-%d %H:%M:%S')
        count = (int(time.mktime(timeStop))-int(time.mktime(timeStart)))/60
        type = jsoni['fn']##型号
        defaultModify = jsoni['lp']
        print("起降地址："+str(start)+"---："+str(stop)+"  起降时间："+str(startDate)+"---"+str(stopDate)+"  航空公司： "+ str(comp) +"  型号："+str(type)+"  价格："+str(defaultModify)+" 时长："+str(count)+"分钟")

def get_json2(date,rk,CK,r):
    '''根据构造出的url获取到航班数据'''
    url='http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=HRB&ACity1=SHA&SearchType=S&DDate1=%s&IsNearAirportRecommond=0&rk=%s&CK=%s&r=%s'%(date,rk,CK,r)
    headers={'Host':"flights.ctrip.com",'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",'Referer':"http://flights.ctrip.com/booking/hrb-sha-day-1.html?ddate1=2018-05-15"}
    headers['Referer']="http://flights.ctrip.com/booking/hrb-sha-day-1.html?ddate1=%s"%date
    req=urllib.request.Request(url,headers=headers)
    res=urllib.request.urlopen(req).read().decode("gb2312")
    dict_content=json.loads(res)
    print(len(dict_content['fis']))
    print(dict_content.keys())
    print(dict_content['fis'][0]['at'])

def get_parameter(date):
    '''获取重要的参数
    date:日期，格式示例：2016-05-13
    '''
    url='http://flights.ctrip.com/booking/hrb-sha-day-1.html?ddate1=%s'%date
    res=urllib.request.urlopen(url).read()
    tree=etree.HTML(res)
    pp=tree.xpath('''//body/script[1]/text()''')[0].split()
    CK_original=pp[3][-34:-2]
    CK=CK_original[0:5]+CK_original[13]+CK_original[5:13]+CK_original[14:]

    rk=pp[-1][18:24]
    num=random.random()*10
    num_str="%.15f"%num
    rk=num_str+rk
    r=pp[-1][27:len(pp[-1])-3]
    print(rk)
    print(CK)
    print(r)

    return rk,CK,r

if __name__=='__main__':
    date='2018-05-15'
    rk,CK,r=get_parameter(date)
    get_json()
#    get_json2(date,rk,CK,r)    
    
#    url = 'https://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=SHA&ACity1=HRB&SearchType=S&DDate1=2018-04-26&IsNearAirportRecommond=0&LogToken=d7810f125c1644839993613d84dc9a86&rk=8.287372302409393052146&CK=75242CF5AA0FD7913EEEBAB938DFC358&r=0.2844713440560481963012'
#    headers = {
#    "Host": "flights.ctrip.com",
#    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
#    "Referer": "http://flights.ctrip.com/booking/SHA-BJS-day-1.html?DDate1=2017-10-22",
#    "Connection": "keep-alive",
#    }
#    res = urllib.request.Request(url,headers=headers)
#    res = urllib.request.urlopen(res).read().decode("gb2312")
#    jsonData = json.loads(res)
#    print(res)