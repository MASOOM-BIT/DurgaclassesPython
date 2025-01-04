#update a dictionary
#to update : d[key]=AssignValue
SampleDict = {'a':'apple','b':'banana','c':'cat'}

SampleDict['a']='Apricot' #Key 'a' is already present thus it simply Update with the new value

print(SampleDict)

SampleDict['d'] = 'Dog' # key 'd' is not available thus it will Update to Dict as new element

print(SampleDict)

#Delete/Remove Key-value form the Dict

#1 . del d[Key]: id specified key is present , then Key value pair will be deleted

del SampleDict['d']

print(SampleDict)

try:
    del SampleDict['e'] #if key is not present in dict while deletion we get KeyError
except KeyError as msg:
    print(msg)

#2. d.clear : To truncate the Dict
sample_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}
print(sample_dict)

sample_dict.clear()
print(sample_dict)

#3. del d : Delete the Whole List
del sample_dict
try:
    print(sample_dict) #NameError if Dic is already deleted
except NameError as msg:
    print(msg)

