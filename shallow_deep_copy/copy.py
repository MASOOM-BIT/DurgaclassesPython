l1=[1,2,3,4,5]
l2=l1
l1.append(6)
print(l1)
print(l2)


# NOTE : if we change the value of l1, the value of l2 will also change because l2 is a reference of l1.

# to avoid this we can use deep copy

l1=[1,2,3,4,5]
l2=l1.copy()
l1.append(6)
print(l1)
print(l2)

# NOTE : if we change the value of l1, the value of l2 will not change because l2 is a copy of l1.

# to avoid this we can use deep copy

l1=[1,2,3,4,5]
l2=l1.copy()
l1.append(6)
print(l1)
print(l2)

# NOTE : if we change the value of l1, the value of l2 will not change because l2 is a copy of l1.


# to avoid this we can use deep copy

l1=[1,2,3,4,5]
l2=l1.copy()
l1.append(6)
print(l1)
print(l2)

import copy
l1=[1,2,3,4,5]
l2=copy.copy(l1)
l1.append(6)
print(l1)
print(l2)
