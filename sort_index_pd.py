#Use of index sort is rearrange the data

import pandas as pd

p = pd.read_csv("test1.csv",squeeze = True,index_col=None)
#print(p)
a= p.sort_values(ascending = False)
print(a)

#sorting in term of indexing
b =p.sort_index(ascending = False)
print(b.head())

#Find the index value
print("*********************************Particular value of index 10*********************************************")
print(p[10])
print("***************************************Find multiple values**********************************************")
print(p[[12,15,50,40]]) # to find particular value
print("************************************Find range of the values********************************************************")
print(p[20:25]) #to find for particular range



