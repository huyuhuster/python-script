# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:25:20 2018

@author: HuYu
"""

import numpy as np
import pandas as pd
import math


#namelist = ['CDCHvCable','CO2','He3','He3Data','N2','Plume','PXDCamareLink','PXDPowerCables','RADMonitor','SVDPower','SVDPowerHV','SVDSignal','TemperatureMonitor','TPC','TPCGasPipe']
#desity = {'CDCHvCable':2.03,'CO2':3.58106,'He3':0.35,'He3Data':0.715,'N2':2.34572,'Plume':0.823,'PXDCamareLink':1.6364,'PXDPowerCables':2.08,'RADMonitor':1.0,'SVDPower':2.032,'SVDPowerHV':1.266,'SVDSignal':.3704,'TemperatureMonitor':1,'TPC':0.037,'TPCGasPipe':1.08}
namelist = ['CDCHvCable','CO2','He3','He3Data','N2','Plume','PXDCamareLink','PXDPowerCables','RADMonitor','SVDPower','SVDPowerHV','SVDSignal','TemperatureMonitor','TPC','TPCGasPipe']
desity = {'CDCHvCable':2.021,'CO2':3.58106,'He3':0.35,'He3Data':0.715,'N2':2.34572,'Plume':0.823,'PXDCamareLink':1.6364,'PXDPowerCables':2.08,'RADMonitor':1.0,'SVDPower':2.032,'SVDPowerHV':1.266,'SVDSignal':.3704,'TemperatureMonitor':1,'TPC':0.037,'TPCGasPipe':1.08}

#namelist = ['Plume']
#desity = {'Plume':0.823}


InnerZ = 1960.0;
OuterZ = 2290.0;
InnerR1 = 1201.1
OuterR1 = 1226.0
InnerR2 = 1415.0
OuterR2 = 1440.0
cellPhi = 360./144.
cellZ = OuterZ-InnerZ
cellR1 = (OuterR1-InnerR1)/3
cellR2 = (OuterR2-InnerR2)/3
cellR = OuterR2-OuterR1
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
    L1 = math.sqrt(InnerZ**2+OuterR1**2)
    L2 = math.sqrt(OuterZ**2+OuterR2**2)
    S[iZ]= cellPhi*Pi*(OuterR2*L2-OuterR1*L1)/360.0/10./10.
    print(iZ,S[iZ],L1,L2)
S=S.reshape(1,1)
print(S)

for name in namelist:
    filename = 'forward_ECL/'+name+'_forward.csv'
    print(filename)
    data = pd.read_csv(filename)
    data=data.fillna(0)
    array = data.values
#    array1=array[0, :]
#    print(array.shape)
#    print(array.dtype)
    dic[name]=array
    Sdic[name]=array*S
    mass_cable[name] = (array*S*desity[name]).sum()
#    print(array*S)
    Mass = Mass+array*S*desity[name]
    print(array[0,1],desity[name],Mass[0,1])

#print(dic)
#print(dic.keys())
#print(Mass.shape)
#V = (OuterZ*(OuterR2**2-InnerR2**2)-InnerZ*(OuterR1**2-InnerR1**2))/3/360/10/10/10
#print(V/3)
V=157.147
Density = Mass/V
#for i in range(144):
#    print(Mass[:,i])
print(Mass[0,1],"  ",Density[0,1],"   ",S[0,0])
print(Mass.sum())
np.savetxt('Mass_Thickness_Density/ECLgaps_forward_Mass.csv',Mass, delimiter = ',')
np.savetxt('Mass_Thickness_Density/ECLgaps_forward_Density.csv',Density, delimiter = ',')