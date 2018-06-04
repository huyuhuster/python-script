# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:25:20 2018

@author: HuYu
"""

import numpy as np
import pandas as pd
import math
Pi = math.pi


#filename = 'mass.csv'
#    print(filename)
data = pd.read_excel('mass.xlsx', 'Sheet1', index_col=None,  na_values=['NA'])
#data = pd.read_csv(filename)
#print(data)
data = data.fillna(0)
print(data)


data['mECLB'] = data['r']**2*Pi*data['rhov']*data['lECLB']*data['nECLB'] + data['rhol']*data['lECLB']*data['nECLB'] + data['w']*data['t']*data['rhov']*data['lECLB']*data['nECLB']
data['mCDCB'] = data['r']**2*Pi*data['rhov']*data['lCDCB']*data['nCDCB'] + data['rhol']*data['lCDCB']*data['nCDCB'] + data['w']*data['t']*data['rhov']*data['lCDCB']*data['nCDCB']
data['mCDCF'] = data['r']**2*Pi*data['rhov']*data['lCDCF']*data['nCDCF'] + data['rhol']*data['lCDCF']*data['nCDCF'] + data['w']*data['t']*data['rhov']*data['lCDCF']*data['nCDCF']
data['mARICHF'] = data['r']**2*Pi*data['rhov']*data['lARICHF']*data['nARICHF'] + data['rhol']*data['lARICHF']*data['nARICHF'] + data['w']*data['t']*data['rhov']*data['lARICHF']*data['nARICHF']
data['mTOPF'] = data['r']**2*Pi*data['rhov']*data['lTOPF']*data['nTOPF'] + data['rhol']*data['lTOPF']*data['nTOPF'] + data['w']*data['t']*data['rhov']*data['lTOPF']*data['nTOPF']
data['mECLF'] = data['r']**2*Pi*data['rhov']*data['lECLF']*data['nECLF'] + data['rhol']*data['lECLF']*data['nECLF'] + data['w']*data['t']*data['rhov']*data['lECLF']*data['nECLF']


#data.loc[data.shape[0]+1]= {'cables':'totalMass', 'mECLB':data['mECLB'].sum(),'mCDCB':data['mCDCB'].sum(),'mCDCF':data['mCDCF'].sum(),'mARICHF':data['mARICHF'].sum(),'mTOPF':data['mTOPF'].sum(),'mECLF':data['mECLF'].sum()}

data.loc['Row_sum'] = data.apply(lambda x: x.sum())

print(data)

print(data['mECLB'].sum())

array = data.values




#print(Mass.shape)
#for i in range(144):
#    print(Mass[:,i])
data.to_excel('Massoftopvolum.xlsx', sheet_name='Sheet1')