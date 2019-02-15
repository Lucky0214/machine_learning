#ploting data from .txt & .csv file
# import csv for the file import

import matplotlib.pyplot as plt
import csv

#empty array
x=[]
y=[]

#File handling to the file

with open('test.txt','r') as csvfile:

#csv.reader is a function to read a file
	plots = csv.reader(csvfile)
	for col in plots:
		x.append(col[0])
		y.append(col[1])

plt.plot(x,y,label='File')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('plot from file')
plt.legend()
plt.show()

