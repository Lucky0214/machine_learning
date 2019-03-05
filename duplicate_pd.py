#use of duplicate value
## it gives first value as false and next same value will be true
#### it return boolen duplicate series
import pandas as pd
df = pd.read_csv("testing.csv")
print(df)


#we can find the duplicated value in a single function name as duplicated() function 

print("*****************************duplicated default command*******************")
mask = df["class"].duplicated()
print(df[mask].head())

print("*********************print keep='last'********************")
mask1 = df["class"].duplicated(keep="last")
print(df[mask1].head())

print("********************print reverse***************************")
mask2 = ~df["class"].duplicated(keep="last")
print(df[mask2].head())


