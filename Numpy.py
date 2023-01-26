import numpy as np
x=np.random.uniform(1,20,20) #creating the random vector of size 20 having only float in the range 1-20
print("Original array:",x)
newarr=x.reshape(4,5) #reshaping the array to 4 by 5
print("\n Reshaped array:",newarr)
newarr1 = np.where(newarr == np.amax(newarr, axis=1).reshape(-1, 1), 0, newarr)  # replacing the max value in each row by 0(axis=1)
print("\n Array after replacing the maximum in each row by 0:",newarr1)