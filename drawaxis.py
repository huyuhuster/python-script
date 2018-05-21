#import cv2   
import numpy as np
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt


#plt.figure(figsize=(1000, 1000))   
ax = plt.subplot(111,projection = 'polar')
ax.set_rgrids(np.arange(0.36,1.0,0.07))
ax.set_thetagrids(np.arange(0,360,2.5))
ax.set_xticklabels([])
ax.set_yticklabels([])
#ax.plot(1,45,'--')
#plt.show()
plt.savefig("exam.jpg",figsize=(1500, 1500)) 


