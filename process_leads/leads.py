import numpy as np

leads = np.array([
    [12, 18, 10, 15, 5],   # Sunday
    [20, 25, 22, 18, 8],   # Monday
    [18, 30, 25, 22, 10],  # Tuesday
    [25, 28, 30, 26, 12],  # Wednesday
    [30, 35, 28, 32, 15],  # Thursday
    [40, 45, 38, 40, 20],  # Friday
    [35, 50, 42, 45, 25]   # Saturday
])

# Task 1: Total leads generated each day
# print(np.sum(leads,axis=1)) #axis =1 for rowwise,0 for column

# Task 2: Total leads from each source in 7 days
# print(np.sum(leads,axis=0))

# Task 3: Highest lead day

# print(np.max(leads,axis=1))

# Task 4: Average leads per source

print(np.average(leads,axis=0))