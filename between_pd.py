# use of between method

import pandas as pd
df = pd.read_csv("testing.csv")
print(df)

#we can find the between value using .between() function
## We can also apply with date,time sequence also
mask = df["no."].between(5,15)
print(df[mask])

