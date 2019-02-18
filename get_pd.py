# .get() is alternative method to extract data from csv file

import pandas as pd

p = pd.read_csv("test1.csv",squeeze = True)
print(p)

print(p.get(10))
print(p.get([15,20,25,30,35,40,45]))

#print(p.get([-20 : -30]))


# Result will give none when it is not exist
#syntax for get(key, default=None)

print(p.get(62))

print(p.get(key = "India", default =" This is not available"))

#In this case, 15 is available but 65 is not in the list 
# So it shows the value of 15 and show 65 as NaN
print(p.get(key = [15,65], default =" This is not available"))

