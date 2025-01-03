# 1. len() : No if elements in tuple

tup1 = (10,20,30,50,None,True,False,'abc',10,10,10,33,11)
print(len(tup1))

#2 .count(x) : No of times elements present in tuple
print(tup1.count(10))

#3. index(x) : index of a particular elements
print(tup1.index(33))
try:
    print(tup1.index(777))
except ValueError as msg:
    print(msg)

#4. Sorted() : To sort element based on natural sorting order
tup2 = (34,55,5,43,343,3)
print(sorted(tup2))
print(type(sorted(tup2))) #List : Tuple is immutable

#5. MIN and MAX value --> works on Homogenous elements only
print(min(tup2))
print(max(tup2))
Tup3 = 'Durga'
print(max(Tup3))
print(min(Tup3))







