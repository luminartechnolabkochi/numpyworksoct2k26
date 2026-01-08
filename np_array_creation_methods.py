# array creation methods
# np.array()
# np.zeros()
# np.ones()
# np.full()
# np.random.rand(size)
# np.random.randint(low,high,(size))
import numpy as np

zeros_array=np.zeros((3,3))
print(zeros_array)

ones_array = np.ones((4,4))

print(ones_array)

five_array=np.full((2,3),5)
print(five_array)

rand_array = np.random.rand(2,4)

print(rand_array)

rand_int_array=np.random.randint(10,15,(3,3))
print(rand_int_array)


