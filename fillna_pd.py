
# use of fillna() function

import pandas as pd

p = pd.read_csv("cricket.csv")
print(p.tail())
print("*********************fillna function use************************")
q=p.fillna(1)
print(q.tail())
print("*************************fillna for particular column***************")
r=(p["5w"].fillna(1))
print(r.tail())

