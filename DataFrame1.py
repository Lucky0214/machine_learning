

import pandas as pd


#Methods are same in DataFrame and Series as well
#same method- head(), tail(), index(), shape(), dtypes()
## The above functions are used in both

p=pd.read_csv("cricket.csv")
print(p)
print(p.shape)



#Methods are only in DataFrame
print("************************************columns are*************************************************")
print(p.columns) #shows no. of column
print("******************************axes are************************************************")
print(p.axes) #shows axes
print("*********************info**********************************************")
print(p.info) #show whole info
print("********************************info as function**********************************")
print(p.info()) #shows brief info
print("*******************************dtype_counts**************************************")
print(p.get_dtype_counts()) #shows dtype and count
