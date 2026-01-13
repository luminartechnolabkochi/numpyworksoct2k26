
"""
stacking

a)verticalstacking
    np.vstack((arr1,arr2))
        1 2 3 4
        10 20 30 40
b)horizontalstacking
    np.hstack((arr1,arr2))
"""



import numpy as np

arr1 = np.array([1,2,3,4])

arr2 = np.array([10,20,30,40])

v_stack_array = np.vstack((arr1,arr2))

print(v_stack_array)

h_stack_array = np.hstack((arr1,arr2))

print(h_stack_array)

two_d_arr1=np.array([[1,2],
                     [3,4]])


two_d_arr2=np.array([[10,20],
                     [30,40]])



"""
rtwo_d_arr1=[
    [1,2],
    [3,4]
]


two_d_arr2=[
    [10,20],
    [30,40]
]

v_stack=[
    [1,2],
    [3,4],
    [10,20],
    [30,40]

]

h_stack=[
    [1,2,10,20],
    [3,4,30,40]
]
"""

