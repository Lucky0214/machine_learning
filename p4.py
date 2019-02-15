

import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 4
means_frank = (90, 55, 40, 65)
means_guido = (85, 62, 54, 20)
means_guid = (25, 98, 24, 30)

 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.20
opacity = 0.8
 
rects1 = plt.bar(index, means_frank, bar_width,
alpha=opacity,
color='b',
label='Frank')

 
rects2 = plt.bar(index + bar_width, means_guido, bar_width,
alpha=opacity,
color='g',
label='Guido')

rects3 = plt.bar(index +(2* bar_width), means_guid, bar_width,
alpha=opacity,
color='r',
label='Guid')

 
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + (2*bar_width), ('Virat', 'Mahi', 'Rohit', 'shikhar'))
plt.legend()
 
plt.tight_layout()
plt.grid()
plt.show()
