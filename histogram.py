#frequency measurement of the one parameter

import matplotlib.pyplot as plt
import numpy as np

ages = [99,15,20,40,55,23,55,44,11,34,62,32,42,1,23,24,60,10,12,18,2]

bins = 10

range = (0,100)

plt.hist(ages,bins,range,color='green',histtype='bar',rwidth=0.7)
plt.xlabel('ages')
plt.ylabel('bins')
plt.title('histogram')
plt.grid()
plt.show()
