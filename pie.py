#Circular way of their distribution

import matplotlib.pyplot as plt
activities = ['eat','sleep','work','play']
slices= [3,7,8,6]
color =['r','g','m','b']

#labels used to block box
#colors used to give color in the pie chart
#startangle is used to starting point
#shadow is for 3D effect
#explode is use to cut slice
#autopct is used to show percentage of individual slice
plt.pie(slices,labels=activities,colors=color,startangle=90,shadow=True,
	explode=(0.1,0,0,0),autopct='%1.2F%%')
plt.legend()
plt.show()
