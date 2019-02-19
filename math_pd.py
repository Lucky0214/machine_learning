#basic math method which is use in every time
#use of .idxmax() & .idxmin()


import pandas as pd

p= pd.read_csv("test.csv", squeeze = True)

print(p)

print( p.count())
print(p.mean())
print(p.sum())

print(p.std())
print(len(p))
print(p.median())
print(p.max())
print(p.min())

# idxmax()
print("Use of idxmax")
print(p.idxmax()) #hold index of maximum value
print("max value")
print(p[p.idxmax()])

print("Use of idxmin")
print(p.idxmin()) #hold index of minimum value
print("min value")
print(p[p.idxmin()])

