# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 11:56:48 2018

@author: HuYu
"""

import numpy as np  
import matplotlib.pyplot as plt  

plt.ylim([-1.5, 1.5])
plt.xlim([-1.5, 1.5])
plt.axis('off')
ax = plt.gca()

1. 关闭坐标刻度
plt.xticks([])
plt.yticks([])
1
2
关闭坐标轴：

plt.axis('off')
#1
#注意，类似的这些操作若想起作用，需要将其置于 plt.show() 之前，plt.imshow() 之后。
#
#2. 设置所要保存图像的 dpi
#dpi：Dots Per Inch
#plt.savefig(..., dpi=150)
#
#3. 坐标轴不可见
#frame = plt.gca()
## y 轴不可见
#frame.axes.get_yaxis().set_visible(False)
## x 轴不可见
#frame.axes.get_xaxis().set_visible(False)


ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))


r = 1.0  
a, b = (0., 0.)  
fig = plt.figure()  
axes = fig.add_subplot(111)

for r1 in np.arange(0.36,r,0.07):
    theta = np.arange(0, 2*np.pi, 0.001)  
    x = a + r1 * np.cos(theta)  
    y = b + r1 * np.sin(theta)  
    plt.plot(x, y)  

#x1 = a + 2*r * np.cos(theta)  
#y1 = b + 2*r * np.sin(theta)  
  
 
axes = fig.add_subplot(111)   
#plt.scatter(x, y,s = 1,marker = 'o')  
#plt.scatter(x1, y1)
#plt.plot(x, y)  
#plt.plot(x1, y1)  
  
axes.axis('equal')  
#plt.show()
plt.savefig("cercle.png",figsize=(1500, 1500)) 