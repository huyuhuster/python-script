#!/usr/bin/env python
import numpy as np   
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from matplotlib.animation import FuncAnimation

#f=open("data_sample.txt","r")
#f=open("/scratchfs/bes/huy/train.txt","r")
f=open("train1.txt","r")
a=[]
for line in f:
#	a=line[12:101*101]
#	a=line.split(',')[2].split(' ')
	a=line.split(' ')
	print len(a), type(a)
#	print a[1]
	break

fig = plt.figure()
ims = []
for i in range(0,15):
        print i
        b=np.array(a[101*101*(4*i+0):101*101*(4*i+1)],dtype=np.int8)
        b.shape=(101,101)

        ax=plt.imshow(b, animated=True)

        ims.append([ax])


ni = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
#ni = animation.FuncAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
#ni.save('line.gif', dpi=80)
plt.show()
