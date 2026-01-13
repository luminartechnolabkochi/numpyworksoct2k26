
import numpy as np


# np.loadtxt(file_path,delimeter=,skip_rows)
data=np.loadtxt("fileworks\\sales_data\\sales.csv",delimiter=",",skiprows=1,dtype="str")

print(data)

units_sold=data[:,3].astype("int")

print(np.sum(units_sold),"total units sold")

# max unit

print("max unit",np.max(units_sold))

# min unit
print("max unit",np.min(units_sold))

# avg unit
print("max unit",np.average(units_sold))

# revenue

revenue= data[:,3].astype("int")*data[:,4].astype("float")

print("item revenue",revenue)

# total revenue

print("Total revenue",np.sum(revenue))

# units sold > 8

print(data[data[:,3].astype("int")>8])
# category == Electronics

print("elevctronics",data[data[:,2]=="Electronics"])


data[:,4]=data[:,4].astype("int")-100

print("discount",data)

# total revenue of north region

# numpy files


#   