# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:25:20 2018

@author: HuYu
"""

import numpy as np
import pandas as pd
import math

namelist = ['CDCHvCable','CO2','He3','He3Data','N2','Plume','PXDCamareLink','PXDPowerCables','RADMonitor','SVDPower','SVDPowerHV','SVDSignal','TemperatureMonitor','TPC','TPCGasPipe']
desity = {'CDCHvCable':2.03,'CO2':3.58106,'He3':0.35,'He3Data':0.715,'N2':2.34572,'Plume':0.823,'PXDCamareLink':1.6364,'PXDPowerCables':2.08,'RADMonitor':1.0,'SVDPower':2.032,'SVDPowerHV':1.266,'SVDSignal':0.3704,'TemperatureMonitor':1,'TPC':0.037,'TPCGasPipe':1.08}
#namelist = ['Plume']
#desity = {'Plume':0.823}


InnerZ = 1938.0;
OuterZ = 1960.0;
InnerR = 1162.0
OuterR = 1245.0
cellPhi = 360./144.
cellZ = OuterZ-InnerZ
cellR = OuterR-InnerR
Pi = math.pi 
print(Pi)
dic={}
Sdic={}
mass_cable={}

#质量
Mass = np.zeros((1,144))

#填充材料密度
Density = np.zeros((1,144))

#填充材料密度(defualt: Cu)
rho = 8.96;   

S = np.zeros(1)
#    print(S)
for iZ in range(1):
    #print(rmin,rmax,rmax**2-rmin**2)
#    S[iZ] = cellPhi*Pi*InnerR*cellR/360.0/10./10.
    S[iZ] = cellPhi*Pi*(OuterR**2-InnerR**2)/360.0/10/10
    print(iZ,S[iZ])
S=S.reshape(1,1)
print(S)

for name in namelist:
    filename = 'forward_Top/'+name+'_forward.csv'
    print(filename)
    data = pd.read_csv(filename)
    data=data.fillna(0)
    array = data.values
    array=array[-1::-1, :]
#    print(array.shape)
#    print(array.dtype)
    dic[name]=array
    Sdic[name]=array*S
    mass_cable[name] = (array*S*desity[name]).sum()
#    print(array*S)
    Mass = Mass+array*S*desity[name]
    print(Mass[0,2])

#print(dic)
#print(dic.keys())
#print(Mass.shape)
Density = Mass/S/(cellZ/10.)
print(S*cellZ/10, cellZ/10)
#for i in range(144):
#    print(Mass[:,i])
print(Mass[0,2],"  ",Density[0,2],"   ",S[0,0])
print(Mass.sum())
np.savetxt('Mass_Thickness_Density/TOP_ECL_forward_Mass.csv',Mass, delimiter = ',')
np.savetxt('Mass_Thickness_Density/TOP_ECL_forward_Density.csv',Density, delimiter = ',')