#Learning drop rows with null value

import pandas as pd

p=pd.read_csv("cricket.csv")
print(p.head())
print(p.tail())
# .dropna(axis=0, how='any', thresh=None,...)
q =p.dropna()
print(q.head())
print(q.tail())

print("****************************use for delete any Nan row*****************************")
r =p.dropna(how="any") #use for delete any Nan row
print(r)
print("****************************use for delete only when all argument are NaN*********************")
s = p.dropna(how="all",inplace=True)#use for delete only when all argument are NaN
print(s)
print(p)

