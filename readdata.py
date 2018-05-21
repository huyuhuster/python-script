#!/usr/bin/env python
import numpy as np
import matplotlib as mpl    
import matplotlib.pyplot as plt
from matplotlib import animation

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
for i in range(5,15):
        print i
        b=np.array(a[101*101*(4*i+0):101*101*(4*i+1)],dtype=np.int8)
        b.shape=(101,101)

        c=np.array(a[101*101*(4*i+1):101*101*(4*i+2)],dtype=np.int8)
        c.shape=(101,101)

        d=np.array(a[101*101*(4*i+2):101*101*(4*i+3)],dtype=np.int8)
        d.shape=(101,101)

        e=np.array(a[101*101*(4*i+3):101*101*(4*i+4)],dtype=np.int8)
        e.shape=(101,101)

        fig = plt.figure()
        ax = fig.add_subplot(221)
        ax.imshow(b)

        ax = fig.add_subplot(222)
        ax.imshow(c)

        ax = fig.add_subplot(223)
        ax.imshow(d)

        ax = fig.add_subplot(224)
        ax.imshow(e)

        plt.show()

def update_line(num, data, line): 
        line.set_data(data[...,:num]) 
        return line,

line_ani = animation.FuncAnimation(fig, update_line, 25,fargs=(b, l),interval=50, blit=True)
plt.show()
