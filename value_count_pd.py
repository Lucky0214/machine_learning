#value_counts function is use the find count of same type of data



import pandas as pd
p = (pd.read_csv("test1.csv"))
print(p)
print(p.value_counts())
