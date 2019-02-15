
#Using of barplot for all the measurement in the y axis

import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [40,50,20,80,77]


plt.xticks(np.arange(10),('tom', 'Dick', 'Harry', 'Sally','hel', 'Sue'))
#tick_label = [ 'one','two','three','four','five' ]
plt.bar(x,y,width=.6,color=['blue'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar Plot')
plt.grid()
plt.show()

