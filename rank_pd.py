#.rank() function is used for given ranking to individual column's value


import pandas as pd

p = pd.read_csv("test.csv").dropna(how="all") #dropna is used for drop NaN value
p["Salary"] = p["Salary"].fillna(0).astype(int) #fillna for full NaN value &  astype is used for type(int/float)
p["Salary"].rank(ascending=False) #rank is used for give ranking by default in ascending order

print(p)

#We make a salary rank on the basis of Salary
p["SalaryRank"]=p["Salary"].rank(ascending=False).astype(int)
q=p.sort_values(by="Salary",ascending=False)
print(q)


#Decide salary wise ranking

