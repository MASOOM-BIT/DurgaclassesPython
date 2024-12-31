SampleTuple = (10,20,30,40,50)
print(type(SampleTuple))
print(SampleTuple)

#Empty Tuple
Tup=()
print(Tup)

#Sigle Value Tuple
# t=(10) -> Not valid : It is not consider as tuple rather than variable
Tup1 = (10)
print(type(Tup1))  #int

Tup2=(10,)
print(type(Tup2))

#multi-value Tuple
SampleTuple = (10,20,30,40,50)
print(type(SampleTuple))
print(SampleTuple)

#Tuple Using Functions
li1=[10,20,30,40]
print(type(li1))
Tup3=tuple(li1)
print(type(Tup3))

#Genrating tuple using range function
t=tuple(range(1,20,2))
print(t)

#Immutability of Tuple

try:
    t[2]=777
except TypeError as msg:
    print(msg)





