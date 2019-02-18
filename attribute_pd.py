
#Attribute will be a series.
#In pandas, string data always be consider as object.
## To extract any type of information inside the series, Will use attributes
### Attribute only get the information but method can change it

import pandas as pd

man = ["handsome", "charm", "humble"]

s = pd.Series(man)

print(s)

#s.value show the list in term of array
t = s.values

#s.index gives start value and end value with step difference
u = s.index

#s.dtype use to check type
v = s.dtype
print(v)
print(u)
print(t)
