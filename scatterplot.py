# To check a data in a particular point

import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]

y=[12,31,54,21,53,46,75,14,21,02]

plt.scatter(x,y,label="stars",color='blue',marker="*",s=30)
plt.xlabel('x-axis')
plt.ylabel('y-lable')
plt.title('Scatter plot')

#if there is more than one output in their plot
#then
#to differentiate all value use legend function

plt.legend() #If we added label in the plot function Then legend calling is mendatory to show the indication block in the plot
plt.grid()
plt.show()
