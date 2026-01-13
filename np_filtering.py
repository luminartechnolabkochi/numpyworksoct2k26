

import numpy as np

productivity = np.array([
#emp 1  2  3  4  5  6  7  8  9  0 
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],#monday
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],#tue
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],#wed
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],#thu
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],#fri
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9] #sat
])


# < 8 = 0
productivity[productivity<8]=0

print(productivity)


# print(productivity[productivity<8])

# # working hours between 5 to 7

# print(productivity[(productivity>=5) & (productivity<=7)])

# # print working hrs of first employee with working hrs < 8

# first_emp_working_hrs=productivity[:,0]

# print(first_emp_working_hrs[first_emp_working_hrs<8])

# # print last two  employees working hrs < 7 

