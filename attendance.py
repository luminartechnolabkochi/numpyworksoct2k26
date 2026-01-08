import numpy as np

attendance = [
  
  #m  t  w  h  f
  [1, 1, 1, 1, 1], # Student 1
  [1, 0, 1, 1, 1], # Student 2
  [1, 1, 0, 1, 1], # Student 3
  [0, 1, 1, 1, 0], # Student 4
  [1, 1, 1, 0, 1], # Student 5
  [1, 0, 0, 1, 1], # Student 6
  [1, 1, 1, 1, 0], # Student 7
  [0, 1, 1, 0, 1], # Student 8
  [1, 1, 0, 1, 0], # Student 9
  [1, 0, 1, 1, 1]  # Student 10
#   

]

# count_nonzero
arr=np.array(attendance)
# functions
# sum,max,min,avg
# axis=0 // column
# axis=1 // row
# arr=np.array(attendance)


# studentwise present count
# print(np.sum(arr,axis=1))

# daywise
# print(np.sum(arr,axis=0))


# display attensdance student3

# print(arr[2])

# display student7 tuesday attendance
# print(arr[6,1])

# display all students friday attendance

# print(arr[:,-1])

# update student10 tuesday attendance as present

# arr[9,1]=1

# print(arr)


student_wise_absent_count = np.count_nonzero(arr==0,axis=1)
print(student_wise_absent_count)

day_wise_absent_count = np.count_nonzero(arr==0,axis=0)
print(day_wise_absent_count) 