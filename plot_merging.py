#Multiple graph in a single plot

import matplotlib.pyplot as plt
import numpy as np

x= np.arange(0,2*np.pi,0.001)
y1= np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,label='sin')
plt.plot(x,y2,label ='cos')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.title('sin & cosin function')
plt.show()

