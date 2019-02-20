

#access the data in different manner

import pandas as pd

p=pd.read_csv("cricket.csv")

print("********************sum column wise******************************")
print(p.sum())
print("******************Another way sum column wise**********************")
print(p.sum(axis=0))
print("********************** way to sum ROW wise*******************")
print(p.sum(axis=1))
print("***********************Another way to sum Row Wise*******************")
print(p.sum(axis="columns"))
#print(p)

#To grap the data
#It works only when there is no gap between any name
print("**********************Extract only Name**************************")
print(p.Name)
print(p.Name.head())
print("*********************Type of Name Data***************************")
print(type(p.Name))

#To grap data if there is some gap
print(p["Name"])
print(p["Team"])

#To grap multiple data in single command

print("***************Print data using List******************************")
print(p[["Name","Team","matches","runs scored"]])

#In the above case, If there is any changes then we change in every point
##So we use Another method for the same
q = ["Name","Team","matches","runs scored"]
print(p[q].head())
