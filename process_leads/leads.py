import numpy as np

import numpy as np

leads = np.array([
   
   [
    # s  m    t  w   th
    [12, 18, 10, 15, 5],   # facebook
    [20, 25, 22, 18, 8],   # insta
    [18, 30, 25, 22, 10],  # youtube
    [25, 28, 30, 26, 12],  # refferal
    [30, 35, 28, 32, 15],  # walkin
    [40, 45, 38, 40, 20],  # reddit
    [35, 50, 42, 45, 25]   # camp
   ]
    
])


# Task 1: Total leads generated each day
# print(np.sum(leads,axis=0))

# Task 2: Total leads from each source 
# print(np.sum(leads,axis=1))

# Task 3: Highest lead day

# day_wise_total=np.sum(leads,axis=0)

# max_total = np.max(day_wise_total)

# print(np.argmax(day_wise_total))


# Task 4: Average leads per source

# print(np.average(leads,axis=1))

# # Task 5: Average leads per day

# print(np.average(leads,axis=0))

# highest lead source

# np.array()
# np.ones((r,c))
# np.zeros((r,c))
# np.full((r,c),value)
# np.random.rand(r,c)
# np.rand.randint(low,high,(r,c))

# function
# np.sum()
# np.max()
# np.avg()
# np.min()
# np.median()
# np.argmax()

# axis=>o [column]
# axis=>1[rows]












# Task 1: Total leads generated each day
# print(np.sum(leads,axis=1)) #axis =1 for rowwise,0 for column

# Task 2: Total leads from each source in 7 days
# print(np.sum(leads,axis=0))

# Task 3: Highest lead day

# print(np.max(leads,axis=1))

# Task 4: Average leads per source

print(np.average(leads,axis=0))