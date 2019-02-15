import numpy as np
list = [1,2,3,4]
print [list]

arr = np.array(list)
print arr

#like a range function but shows in form of array
arrq = np.arange(0,10)
print arrq

#print only even value
arrq = np.arange(0,10,2)
print arrq

#matrix as zeros
arrq = np.zeros((5,10))
print arrq

#matrix as ones
arrq = np.ones((5,10))
print arrq

#matrix with random number
arrq = np.random.randint(0,1000,(5,5))
print arrq

#matrix with random number with constant number using random.seed(101)
np.random.seed(101)
arrq = np.random.randint(0,1000,(5,5))
print arrq
print arrq.max()
print arrq.min()
print arrq.mean()
print arrq.argmax() #position of max number
print arrq.argmin() #position of minimum number
print arrq.reshape(2,2) #change the dimension
