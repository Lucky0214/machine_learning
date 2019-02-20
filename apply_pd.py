#apply function
# when we need to apply a function in each value then we use .apply function


import pandas as pd

p=pd.read_csv("test.csv", squeeze=True)
def classify_per(number):
	if number<100:
		return "OK"
	elif number>=100 and number<500:
		return "still OK"

	else:
		return "bad"

print("*******************************It return Status of the number*******************************************")
q = p.apply(classify_per)
print(q.head(10))






