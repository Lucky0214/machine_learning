
import pandas as pd

df = pd.DataFrame({'year': [2015, 2016], 'month': [2, 3], 'day': [4, 5]})
print( pd.to_datetime(df))
