
import numpy as np

sevens_array= np.full((5,7),7)

print(sevens_array)

zerors_array = np.zeros((3,3),dtype="int16")

zerors_array[1,1]=1
print(zerors_array)

sevens_array[1:4,2:5]=zerors_array
print(sevens_array)