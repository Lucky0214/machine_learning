
#Broadcasting in pandas
# We can perform action in a particular series in column
## Same operation for whole series

import pandas as pd

p= pd.read_csv("test.csv")

print(p.head())
q = p["Name"]-10
r = p["Name"].add(10)
print(q.head())
print(r.head())
