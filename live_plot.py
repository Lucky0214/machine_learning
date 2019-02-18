import matplotlib.animation as ani
from matplotlib import style
#import matplotlib.style
import matplotlib.pyplot as plt


plt.style.use('fivethirtyeight')

fig1 =plt.figure()

ax1 = fig1.add_subplot(1,1,1)

def animate(p):
	line_data = open('test.txt','r').read()

	plot_data = line_data.split('\n')
	x1=[]
	y1=[]

	for line in plot_data:
		if len(line)>1:
			x,y =line.split(',')
			x1.append(x)
			y1.append(y)

		ax1.clear()
		ax1.plot(x,y)

anime_data = ani.FuncAnimation(fig1,animate, interval = 500)
plt.show()
