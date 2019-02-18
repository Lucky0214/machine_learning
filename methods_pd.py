
# Use of method , parameter , Arguments
# method required paranthesis

import pandas as pd

rate = [2.99,3.54,2.65,15.12,24.15,25.2]

print(pd.Series(rate))
r = pd.Series(rate)

print(r.sum())
print(r.product())
print(r.mean())

fruits = ['apple','orange','banana','grape','papaya']
weeks = ['sunday','monday','tuesday','wednesday','thursday']

#syntax for Series function
#pd.Series(data=none, index = none, dtype = none, name = none, copy = false)

print(pd.Series(fruits,weeks))
print(pd.Series(data = fruits, index = weeks))
print(pd.Series(fruits, index = weeks))
