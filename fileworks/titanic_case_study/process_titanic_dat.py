
import numpy as np

data = np.genfromtxt("fileworks\\titanic_case_study\\passenger_data.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")

# total number of passengers
print(f"total number of passengers {data.shape}")

# survival analysis

# total number of survivals
# total numvber of death
