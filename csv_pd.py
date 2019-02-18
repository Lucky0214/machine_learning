# CSV stand for comma separate value
# we can do the same thing with MS Excel but it has limit in excel.
# We did work with pandas library easily for big data also 
# Sorting Method
#inplace parameter


import pandas as pd


#squeeze is for pandas format
#usecols is used for particular column

p = pd.read_csv("test1.csv",squeeze = True)

#head is a method to check first five value
#tail is a method to check last five value
q = p.head()
s = p.head(10)
r = p.tail()
#q = pd.read_csv("movie.csv",squeeze = True)
print(s)
print(p)
print(q)
print(r)
print(p.values) #print all the values
print(p.index) # print index
print(p.is_unique) #to check all the value is unique or not, if unique returns True
print(p.ndim) # to check dimension
print(p.name)
print(p.shape) # to check shape of the data
print(p.sort_values().head()) #ascending order
#there is only way to descending order
print(p.sort_values(ascending = False).head()) #descending order

#inplace is used for to replace data
value = p.sort_values(ascending = False,inplace=True)
print(value)


