
import numpy as np

data = np.genfromtxt("fileworks\\titanic_case_study\\passenger_data.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")

print(data.shape)

