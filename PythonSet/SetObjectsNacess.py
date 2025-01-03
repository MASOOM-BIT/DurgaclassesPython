#Duplication Not Allowed
#index is not present thus Accessing with index and Slicing is not Allowed | order is not present
#mutable
#uses : {}

s1={10,20,30,40,50,'abc','AAA',None,True,False}
print(type(s1))
print(s1) # No Order in Output

#Index accessing is not allowed
try:
    print(s1[0])
except TypeError as msg:
    print(msg)
# Slicing is not Allowed
try:
    print(s1[0:5:2])
except TypeError as msg:
    print(msg)

#Using set() function
#using string
s2=set('Durga') #No Order in this as well
print(s2)
#using range
s3 = set(range(1,10))
print(s3)
#using list
li1=[10,20,30,None,True]
print(set(li1))

#empty Set

s={} # By default, it is considered as Dictionary
#{} is also used in creation of dictionary data type thus to distinguish between there both empty set/dict..
#we use set function to create empty set

Emptyset = set()

#Proof of Duplication removal

li1 = [10,20,300,10,10,10]
s=set(li1)
print(s)

