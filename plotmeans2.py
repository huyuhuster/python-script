import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import datetime
import sys
import matplotlib.cbook as cbook

ma,m,l = loadtxt('ml2.csv', delimiter=',', usecols=(0,1,2), unpack =True)
#means = m[0:2000]
#lables = l[0:2000]
meansa = ma
means = m
lables = l
print means
print lables
plt.xlabel("Means_all")
plt.ylabel("Means")
#plt.ylabel("Lables")
plt.scatter(meansa,means,s=lables)
plt.show()

#fig, ax = plt.subplots()
#ax.scatter(delta1[:-1], delta1[1:], s=la, alpha=0.5)
