# isin() function provides multiple arguments

import pandas as pd

df = pd.read_csv("testing.csv")
print(df)

#We are taking same concept which is not better for coder

mask1 = df["class"] =="a"   #mask is used for finding same type in a perticular column
print(df[mask1])

mask2 = df["class"] == "b"
mask3 = df["class"] == "c"

print(df[ mask1 | mask2 | mask3])

#Above concept in a single line
print("*****************Code optimize concept with isin function*************************")
mask = df["class"].isin(["a","b","c"])
print(df[mask])
