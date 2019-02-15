import numpy as np
import matplotlib.pyplot as plt

#line plot with numpy
t = np.arange(0.0,2.0,0.01) # x-axis
s = 1 + np.cos(2*np.pi*t) # y-axis
plt.plot(t,s,'*') # * is for design of graph
plt.grid() #grid in the back ground
plt.xlabel('time(s)')
plt.ylabel('voltage(mV)')
plt.title('line plot with numpy')

plt.show()
