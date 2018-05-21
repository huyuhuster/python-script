import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import datetime
import sys
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
plt.scatter(meansa,means,c=lables)
plt.show()
