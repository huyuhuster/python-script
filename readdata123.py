#!/usr/bin/env python
import numpy as np
import numpy as np   
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#f=open("data_sample.txt","r")
#f=open("/scratchfs/bes/huy/train.txt","r")
f=open("train1.txt","r")
a=[]
j=0
for line in f:
#	a=line[12:101*101]
#	a=line.split(',')[2].split(' ')
	a=line.split(' ')
	print len(a), type(a)
	break
#	print a[1]

fig = plt.figure()
ims = []
for i in range(0,14):
        print i
        b=np.array(a[101*101*(4*i+0):101*101*(4*i+1)],dtype=np.int8)
#        print b.shape
        b.shape=(101,101)

        c=np.array(a[101*101*(4*i+1):101*101*(4*i+2)],dtype=np.int8)
        c.shape=(101,101)

        d=np.array(a[101*101*(4*i+2):101*101*(4*i+3)],dtype=np.int8)
        d.shape=(101,101)

        e=np.array(a[101*101*(4*i+3):101*101*(4*i+4)],dtype=np.int8)
        e.shape=(101,101)

        ax = fig.add_subplot(221)
        ax.imshow(b,animated=True)

        ax = fig.add_subplot(222)
        ax.imshow(c,animated=True)

        ax = fig.add_subplot(223)
        ax.imshow(d,animated=True)

        ax = fig.add_subplot(224)
#        ax.imshow(e,animated=True)

        ims.append([ax])


ni = animation.ArtistAnimation(fig, ims, interval=100, blit=True, repeat_delay=1000)
plt.show()
