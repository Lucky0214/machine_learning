# use of drop_duplicated() method
## It drops the duplicate value after identify
import pandas as pd
df = pd.read_csv("testing.csv")
print(df)
print(len(df))

#we can find the duplicated value in a single function name as duplicated() function 

print("*****************************drop duplicated default command*******************")
mask = df.drop_duplicates(subset="class")
print(mask)
print(len(mask))

print("*********************subset is use as or command********************")
print("***********It will print as either class or no. ****************")
print("*************In this case, subset work as OR operator******************")
mask1 = df.drop_duplicates(subset=["class","no."],keep="last")
print(mask1)

print("********************print reverse***************************")
mask2 = ~df["class"].duplicated(keep="last")
print(df[mask2].head())


