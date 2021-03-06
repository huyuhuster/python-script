# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:25:20 2018

@author: HuYu
"""

import numpy as np
import pandas as pd
import math

namelist = ['CLAWS','CO2','FLANGS','FLANGSpower','He3','He3Data','INVCable','N2','PXDCamareLink','PXDPowerCables','RADMonitor','SVDPower','SVDPowerHV','SVDSignal','TemperatureMonitor','TPC','TPCGasPipe']
desity = {'CLAWS':3.567,'CO2':3.58106,'FLANGS':0.006,'FLANGSpower':0.035,'He3':0.35,'He3Data':0.715,'INVCable':1,'N2':2.34572,'PXDCamareLink':1.6364,'PXDPowerCables':2.08,'RADMonitor':1.0,'SVDPower':2.032,'SVDPowerHV':1.266,'SVDSignal':.3704,'TemperatureMonitor':1,'TPC':0.037,'TPCGasPipe':1.08}
#namelist = ['Plume']
#desity = {'Plume':0.823}


InnerR = 451.0;
OuterR = 1240.0;
cellPhi = 360./144.
cellR = (OuterR-InnerR)/16
Pi = math.pi 
print(Pi)
dic={}
Sdic={}
mass_cable={}

#质量
Mass = np.zeros((16,144))

#填充材料厚度
Thickness = np.zeros((16,144))

#填充材料密度(defualt: Cu)
rho = 8.96;   

S = np.zeros(16)
#    print(S)
for iR in range(16):
    rmin = (InnerR + iR*cellR)/10.
    rmax = (InnerR + (iR+1)*cellR)/10.
    #print(rmin,rmax,rmax**2-rmin**2)
    S[iR]= cellPhi*Pi*(rmax**2-rmin**2)/360.0
    #print(iR,S[iR])
S=S.reshape(16,1)
print(S)

for name in namelist:
    filename = 'backward/'+name+'_backward.csv'
    print(filename)
    data = pd.read_csv(filename)
    data=data.fillna(0)
    array = data.values
    array = array[-1::-1, :]
#    print(array.shape)
#    print(array.dtype)
#    print(array)
    dic[name]=array
    Sdic[name]=array*S
    mass_cable[name] = (array*S*desity[name]).sum()
#    print(array*S)
    Mass = Mass+array*S*desity[name]
    print(Mass[0,0],desity[name],array[0,0])

#print(dic)
#print(dic.keys())
#print(Mass.shape)
Thickness = Mass*10/rho/S
#for i in range(144):
#    print(Mass[:,i])
print(Mass.sum())
print(Mass[0,0],"  ",Thickness[0,0],"   ",S[0,0])
np.savetxt('Mass_Thickness_Density/CDC_ECL_backward_Mass.csv',Mass, delimiter = ',')
np.savetxt('Mass_Thickness_Density/CDC_ECL_backward_Thickness.csv',Thickness, delimiter = ',')



