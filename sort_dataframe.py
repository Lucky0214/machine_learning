# .sort_values() is use for 1D array for data sorting
## We can sort the array in multi-dimension array

import pandas as pd

p = pd.read_csv("test.csv")

#It send NaN value at the last of the date by default
print(p.sort_values("Name",ascending=False))

#NaN position function = na_position
print(p.sort_values("Name",ascending=False, na_position="first"))

