# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:25:20 2018

@author: HuYu
"""

import numpy as np
import pandas as pd
#import math

namelist_f = ['CDC_ECL_forward_Thickness','ARICH_TOP_forward_Density','ECLgaps_forward_Density','TOP_ECL_forward_Density']
namelist_b = ['CDC_ECL_backward_Thickness','ECLgaps_backward_Density']

#Pi = math.pi 
#dic={}
#Sdic={}

for name in namelist_f:
    filename_in = 'Mass_Thickness_Density/'+name+'.csv'
    filename_out = 'Mass_Thickness_Density/'+name+'_conversion.csv'
#    print(filename_in)
    data = pd.read_csv(filename_in,header=None)
    data=data.fillna(0.0)
#    print(data)
#    print(data.loc[6])
    array = data.values
    array_con=np.hstack((array[: , 36:144],array[: , 0:36]))
    array_con=array_con[:,-1::-1]
    array_0 = np.zeros(144)
    array_0 = array_con
    if name == 'ECLgaps_forward_Density':
        array_con = np.vstack((array_0,array_con))
        array_con = np.vstack((array_0,array_con))
        array_con = array_con/3.
    print(array_con.shape)
    print(array_con.dtype)
    np.savetxt(filename_out,array_con, delimiter = ',')
    

for name in namelist_b:
    filename_in = 'Mass_Thickness_Density/'+name+'.csv'
    filename_out = 'Mass_Thickness_Density/'+name+'_conversion.csv'
    print(filename_in)
    data = pd.read_csv(filename_in,header=None)
    data=data.fillna(0.0)
#    print(data)
#    print(data.loc[6])
    array = data.values
    array_con = np.hstack((array[: , 108:144],array[: , 0:108]))
#    array_0 = np.zeros(144)
    array_0 = array_con
    if name == 'ECLgaps_backward_Density':
        array_con = np.vstack((array_0,array_con))
        array_con = np.vstack((array_0,array_con))
        array_con = array_con/3.
    print(array_con.shape)
    print(array_con.dtype)
    np.savetxt(filename_out,array_con, delimiter = ',')
