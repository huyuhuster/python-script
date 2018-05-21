# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:58:54 2018

@author: HuYu
"""

import matplotlib.pyplot as plt

import numpy as np


fig = plt.figure(figsize=(8, 8))
""" For backward CDC plate """
#Rmin =  451
#Rmax =  1240
""" For forward CDC plate """
Rmin = 437.
Rmax = 1162.

plt.ylim([-Rmax, Rmax])
plt.xlim([-Rmax, Rmax])
plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0)

#plt.grid(True)
plt.axis('off')
ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))


#n = 3
for n in np.arange(Rmin, Rmax, (Rmax-Rmin)/17):
    theta = np.arange(0, 2 * np.pi, np.pi/1000)
#    x0 = (n + 1) / n * np.cos(theta)
#    y0 = (n + 1) / n * np.sin(theta)
    x0 = n * np.cos(theta)
    y0 = n * np.sin(theta)
    plt.plot(x0, y0,'k')

i=0
for theta in np.arange(0, 2 * np.pi, 2*np.pi/144):
    r = np.arange(Rmin, Rmax, (Rmax-Rmin)/17)  
    x0 = r * np.cos(theta)
    y0 = r * np.sin(theta)
    if i%9==0:
        plt.plot(x0, y0,'r')
    else:
        plt.plot(x0, y0,'k')
    i=i+1

#x = np.cos(theta) + 1 / n * np.cos(n*theta)
#y = np.sin(theta) - 1 / n * np.sin(n*theta)
#plt.plot(x, y )

#plt.show()
#plt.savefig("Backwardgrid.png",dpi=500)
plt.savefig("Forwardgrid.png",dpi=500)
