import numpy as np


arr = np.loadtxt(
    "fileworks\\student.txt",
    delimiter=",",
    skiprows=1
)
print(arr)