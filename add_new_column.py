

#Learn to add new column in a .csv file
## Use Raw method to insert in the end
### Use professional method to insert middle

import pandas as pd
p=pd.read_csv("cricket.csv")
print(p.head())

#Raw method to add
print("**********Raw method to add new column*************")
p["Sport"] = "Cricket"
print(p.head())

#Professional method to add
##p.insert(loc, column, value, ...)
### In this method, We can insert column in any position of .csv file
p.insert(3,column="Game",value="Official")
print(p.head())

