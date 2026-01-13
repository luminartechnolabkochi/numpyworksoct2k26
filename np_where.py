

# np.where(condtion,true_vale,false_value)

import numpy as np


ages=np.array([19,20,17,21,23,15])


print(np.where(ages>=20,"Adults","teen"))


# task1
array=np.array([2,3,4,5,6,7,8])

print(np.where(array%2==0,"even","odd"))
# [even,odd,even,odd,,,,,]

# task2

array=np.array([-1,2,3,-1,5,-6])
# [-ve,+ve,+ve]
print(np.where(array>0,"+ve","-ve"))