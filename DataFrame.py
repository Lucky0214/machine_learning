#import the pandas library and aliasing as pd
#import pandas as pd
#data = [1,3,6,4,5,7]
#df = pd.DataFrame(data)
#print(df)


#DataFrame is a multi dimension array

import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data series is:")
print (df)
