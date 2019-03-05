# Filtering
##Wrong dtype takes more memory
### Date - to_datetime
### Time - to_datetime
### True/False - bool
### Gender - Category

##########################Direct Way to Change the Object#############################

#p["Result"]= (p["Result"].astype("bool"))
#p["Date"] = (pd.to_datetime(p["Date"]))
#p["Time"]= (pd.to_datetime(p["Time"]))
#p["Gender"]=(p["Gender"].astype("category"))


#############################Direct change the date & time###############################
#p=pd.read_csv("school.csv", parse_dates=["Date","Time"])



#I could not run the program due to some unknown issue
## Try This Thank You!


import pandas as pd

p=pd.read_csv("school.csv")#, parse_dates=["Date","Time"])
print(p)
print(p.info())
q = p["Result"]
print(q)
#print(p["Result"])
#p["Result"]= (p["Result"].astype("bool"))
#p["Date"] = (pd.to_datetime(p["Date"]))
#p["Time"]= (pd.to_datetime(p["Time"]))
#p["Gender"]=(p["Gender"].astype("category"))

#print(p.info())
