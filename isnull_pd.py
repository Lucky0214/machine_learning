# Using of isnull() method and notnull() method

import pandas as pd

df = pd.read_csv("testing.csv")
print(df)

print("**********isnull function is for showing null data******************")
print("**********************isnull method implemented********************")
mask = df["roll"].isnull()
print(df[mask])


print("**********************notnull() is for showing not null data**********")
mask = df["roll"].notnull()
print(df[mask])
