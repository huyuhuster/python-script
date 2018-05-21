##!/usr/bin/env python
import numpy as np
import sys
import matplotlib.pyplot as plt
f1=open("train1.txt","r")
f2=open("lable.txt","r")
#f3=open("/scratchfs/bes/huy/lable.txt","w")
a=[]
means=np.zeros(101, dtype=float)
lables=np.zeros(101, dtype=float)
i=0
for line in f1:
#while f1.readline():
#       line=f1.readline()
#       a=line[12:101*101]
#       a=line.split(',')[2].split(' ')
#       print len(a), type(line)
#       print float(a[1])+float(a[2])
#       break
        print ("i= ",i)
#       if i<101: continue
        a=line.replace('\n','').split(' ')
#       a=line.split(',')[1]
#       print ("a[0]=",a[0],"a[1]=",a[1],"a[0][0][0]=",a[0][0][0])
#       print ("len(a)= ",len(a),"len(a[0])= ",len(a[0]),"type(a)=", type(a))
        a1=[int(ai) for ai in a]
        c=np.array(a1)
        means[i]=np.mean(c)
        print ("c len:",np.size(c),means[i],)
#        f2.write("\t"+b)
#       f3.write(b+'\n')
        i=i+1
        if i>100:
             break
            
j=0            
for line2 in f2:
#    print line2.replace('\n','')
    lables[j]=line2.replace('\n','')
    j=j+1
    if j>100:
        break
    
    

    
plt.scatter(means,lables)
plt.show()
#n = 1024
#X = np.random.normal(0,1,n)
#Y = np.random.normal(0,1,n)
#plt.scatter(X,Y)
#plt.show()
