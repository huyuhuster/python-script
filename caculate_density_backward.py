# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:25:20 2018

@author: HuYu
"""

import numpy as np
import pandas as pd
import math

namelist = ['CLAWS','CO2','FLANGS','He3','He3Data','INVCable','N2','PXDCamareLink','PXDPowerCables','RADMonitor','SVDPower','SVDSignal','TemperatureMonitor','TPC','TPCGasPipe']
desity = {'CLAWS':1,'CO2':1.633,'FLANGS':1,'He3':0.827,'He3Data':0.715,'INVCable':1,'N2':0.747,'PXDCamareLink':1.6364,'PXDPowerCables':2.08,'RADMonitor':1.0,'SVDPower':2.032,'SVDSignal':.3704,'TemperatureMonitor':1,'TPC':1,'TPCGasPipe':1}
#namelist = ['CO2','FLANGS','He3','He3Data','INVCable','N2','PXDCamareLink','PXDPowerCables','RADMonitor','SVDPower','SVDSignal','TemperatureMonitor','TPC','TPCGasPipe']
#desity = {'CO2':1.633,'FLANGS':1,'He3':0.827,'He3Data':0.715,'INVCable':1,'N2':0.747,'PXDCamareLink':1.6364,'PXDPowerCables':2.08,'RADMonitor':1.0,'SVDPower':2.032,'SVDSignal':.3704,'TemperatureMonitor':1,'TPC':1,'TPCGasPipe':1}
InnerR = 564;
OuterR = 1000;
cellPhi = 360./144.
cellR = (OuterR-InnerR)/16
Pi = math.pi 
print(Pi)
dic={}
Sdic={}
Mass=np.zeros((16,144))
for name in namelist:
    filename = 'backward/'+name+'_backward.csv'
    print(filename)
    data = pd.read_csv(filename)
    data=data.fillna(0.0)
#    print(data)
#    print(data.loc[6])
    array = data.values
    array=array[-1::-1, :]
    print(array.shape)
    print(array.dtype)
#    print(array)
    S = np.zeros(16)
#    print(S)
    for iR in range(16):
        rmin = (InnerR + iR*cellR)/10.
        rmax = (InnerR + (iR+1)*cellR)/10.
        #print(rmin,rmax,rmax**2-rmin**2)
        S[iR]= cellPhi*Pi*(rmax**2-rmin**2)/180.0
    print(S)
    S=S.reshape(16,1)
    dic[name]=array
    Sdic[name]=array*S
#    print(array*S)
    Mass = Mass+array*S*desity[name]

#print(dic)
#print(dic.keys())
print(Mass.shape)
for i in range(144):
    print(Mass[:,i])
np.savetxt('backward/Mass.csv',Mass, delimiter = ',')