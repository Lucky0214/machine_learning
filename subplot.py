import numpy as np
import matplotlib.pyplot as plt

x1=np.linspace(0.0,5.0)
x2 = np.linspace(0.0,2.0) #function for the linear space
y1 = np.sin(2*np.pi*x1)*np.exp2(-x1)
y2 = np.sin(2*np.pi*x2)
plt.subplot(2,1,1) #subplot(row,column,first position for x1,y1) 
plt.plot(x1,y1,'o-') #o- stands for line style
plt.title('plot subplot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.subplot(2,1,2)
plt.plot(x2,y2,'.-')
plt.title('subplot x2,y2')
plt.xlabel('x2-axis')
plt.ylabel('y2-axis')

plt.grid()
plt.show()
