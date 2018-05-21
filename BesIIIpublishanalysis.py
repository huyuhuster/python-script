# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:48:01 2018

@author: HuYu
"""
"""
http://python.jobbole.com/88350/
"""
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
 
def getStockList(df2,slist, stockURL):
#    html = getHTMLText(stockURL)
    html = open(stockURL, 'r', encoding='utf-8')
    #print("html",html)
    htmlhandle = html.read()
    #print("htmlhandle",htmlhandle)
    soup = BeautifulSoup(htmlhandle, 'lxml') 
    Table = soup.find_all('table')
    for table in Table:
        row = {'Status':'', 'Created date':'', 'HN Link':'', 'Submitted date':'', 'Released date':'', 'Deadline':'', 'Author':'', 'Referees':''}
        tr = table.find_all('tr')
        for i in tr:
            tdi = i.find_all('td',attrs={"width":"12%"})
            if len(tdi)>0:
                pattern = re.compile(r':')
                tdix = ''.join(re.split(pattern, tdi[0].text)).strip()
                tdp = i.find_all('td',attrs={"width":"81%"})
                if len(tdp)>0:
                    if tdix in slist:
                        tdpx=re.sub("\n", "", str(tdp[0].text.strip()))
                        tdpx=re.sub("&nbsp", "",tdpx)
                        tdpx=re.sub("\(expired\)", "",tdpx)
                        tdpx=re.sub("\(Confirmed\)", "",tdpx)
                        tdpx=tdpx.strip()
#                        row[tdix]= tdp[0].text.strip()
                        row[tdix]= tdpx
        if row['Author']!='':
            df2.loc[df2.shape[0]+1] = row
 
 
def main():
    input_file = 'D:/爬虫乐园/BESIII Physics Papers.html'
#    output_file = 'D:/爬虫乐园/view-source_hnbes3.ihep.ac.cn_publications_php.php.html'
    slist=['Status', 'Created date', 'HN Link', 'Submitted date', 'Released date', 'Deadline', 'Author', 'Referees']
    df2 = pd.DataFrame(columns=['Status', 'Created date', 'HN Link', 'Submitted date', 'Released date', 'Deadline', 'Author', 'Referees'])
    getStockList(df2,slist, input_file)
#    print(df2.loc[[4],'Deadline'])
    print(df2)
 
main()