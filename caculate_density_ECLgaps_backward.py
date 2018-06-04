# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:25:20 2018

@author: HuYu
"""

import numpy as np
import pandas as pd
import math


namelist = ['CDCCAT7Cable','CDCLVCable','CDCOpticalFiber2C','CDCTRGOpticalFiber12C','CLAWS','CO2','FLANGS','FLANGSpower','He3','He3Data','INVCable','N2','PXDPowerCables','RADMonitor','SVDPower','SVDPowerHV','SVDSignal','TPC','TPCGasPipe']
desity = {'CDCCAT7Cable':2.47,'CDCLVCable':0.97,'CDCOpticalFiber2C':2.47,'CDCTRGOpticalFiber12C':2.31,'CLAWS':3.567,'CO2':3.58106,'FLANGS':0.006,'FLANGSpower':0.035,'He3':0.35,'He3Data':0.715,'INVCable':1,'N2':2.34572,'PXDPowerCables':2.08,'RADMonitor':1.0,'SVDPower':2.032,'SVDPowerHV':1.266,'SVDSignal':0.3704,'TPC':0.037,'TPCGasPipe':1.08}



InnerZ = -1220.0;
OuterZ = -1020;
InnerR1 = 1195.0
OuterR1 = 1267.0
InnerR2 = 1454.0
OuterR2 = 1530.0
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
#    print(iZ,S[iZ],L1,L2)
S=S.reshape(1,1)
#print(S)

for name in namelist:
    filename = 'backward_ECL/'+name+'_backward.csv'
#    print(filename)
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
#    print(array[0,0],desity[name],Mass[0,0])

print( mass_cable)
#print(dic.keys())
#print(Mass.shape)
#V = (OuterZ*(OuterR2**2-InnerR2**2)-InnerZ*(OuterR1**2-InnerR1**2))/3/360/10/10/10
#print(V/3)
V=288.015
Density = Mass/V
#for i in range(144):
#    print(Mass[:,i])
print(Mass[0,0],"  ",Density[0,0],"   ",S[0,0])
print(Mass.sum())
np.savetxt('Mass_Thickness_Density/ECLgaps_backward_Mass.csv',Mass, delimiter = ',')
np.savetxt('Mass_Thickness_Density/ECLgaps_backward_Density.csv',Density, delimiter = ',')




#caculate mass
l = 33.04    
densitya = [3.09,1.,0.944, 0.944, 8.96, 7.874, 4.95,3.5,0.95]
s = [0.2*0.2*Pi, 0.62*0.19,0.5*0.3,0.2*0.2*Pi, (0.3*0.3-0.2*0.2)*Pi, (0.8*0.8-0.7*0.7+0.2*0.2-0.1*0.1-0.8*0.8-0.5*0.5)*Pi,0.3175*0.3175*Pi,0.4*0.4*Pi,0.25*0.25*Pi]
numa = [150,600,300,300,4,8,2,8,8]
densityl = [2.54,0.81,0.63,2.6,1.44,0.43,0.53659,0.1,0.59,3.05]
numl = [6,6,1,8,4,2,2,4,30,3]
print(len(densitya),len(s),len(numa),len(densityl),len(numl))
densitya = np.array(densitya)
s=np.array(s)
numa = np.array(numa)
densityl = np.array(densityl)
numl = np.array(numl)

mass1 = (densitya*s*l*numa) 
mass2 = (densityl*l*numl)
print(mass1/1000.,mass2/1000.,"kg")
    
    
    
    
    
    