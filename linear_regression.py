# Practice of Linear Regression
#%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("testing.csv")
print(data)
x = data["no."]
y = data["roll"]
print(x)
print(y)

mean_x = np.mean(x)
print(mean_x)
mean_y = np.mean(y)
 
n = len(x)

nume = 0
denome = 0
for i in range(n):
	nume =((x[i] - mean_x)*(y[i] - mean_y))
	print(nume)
	demome = ((x[i] - mean_x)**2)
	print(denome)

b1 = (nume / denome)
b0 = (mean_y - (b1*mean_x))

print(b1)
print(b0)


