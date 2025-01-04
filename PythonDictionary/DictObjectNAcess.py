#key-Value Pair
#duplicate Keys are not allowed But Duplicate values are allowed
#Hetrogenous, Unordered , mutable
#indexing and Slicing is not allowed
#-----------------------------------------------------------------------------
# Empty Dict :
dict1 = {}
dict2 = dict()
print(type(dict1))
print(type(dict2))

# Adding Value in Dict : dict variable[Key] = value
dict1[100] = 'durga'
dict1[200] = 'ravi'
dict2[100] = 45664
dict2[200] = True
print(dict1)
print(dict2)

#If the Value is Known

dict3 = {'a':'apple','b':'banana','c':'cat'}
print(dict3)

#Accessing the Element of dict
#Based on keys:
print(dict1[100])
print(dict2[200])
print(dict3['a'])

#from Keyboard
rec={}
n=int(input("Enter the No of Student you Want to Add : "))
i=1
while i<=n:
    name = input("Name of the Student : ")
    marks = float(input("Enter the Marks of Student : "))
    rec[name] = marks
    i=i+1

print("Name of student","\t","Percentage of Marks")
for k,v in rec.items():
    print(k,'\t\t\t',v)

#multiple values in single key

list1 = ['durga','ravi','sunny']
dict4={100:list1}
print(dict4)
