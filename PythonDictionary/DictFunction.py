#1. dict() : To Create empty list
d1 = dict({100:'durga',200:'sunny'})
print(d1)

#2. Create a dict with tuple
d2 = dict([(100,'durga'),(200,'Ravi'),(300,'Shiva')])#List of Tuple
print(d2)

d3 = dict(((100,'durga'),(200,'Ravi'),(300,'Shiva')))#Tuple of tuple
print(d3)

d4 = dict({(100,'durga'),(200,'Ravi'),(300,'Shiva')}) #set of tuple #order not preserved
print(d4)

#3.len(dict) : No of Entries in dict | No of k-v pairs
print(len(d1))
print(len(d2))
print(len(d3))
print(len(d4))

#4.Dict.get(key) : Get the value of keys

print(d3.get(100))
print(d3.get(200))
print(d3.get(300))

print(d3.get(500)) #return None if Key is not present
# dict.get(key,default value)
print(d3.get(600,'Sunny')) #If key not present default value will be Inserted
print(d3.get(100,'Sunny')) #IF ley is present it will give the value present in dict

#5. dict.pop(Keys) : pop the key from dict and return the value
print(d3.pop(100)) #durga pop

#6. dict.popitems() : one k-v will be removed random and its value will be return

print(d3.popitem())
d4={}
try:
    print(d4.popitem()) #if dict is empty Key Error
except KeyError as msg:
    print(msg)

#7. dict.keys() : return Only keys

print(d3.keys())

#8. dict.values : return only all values
print(d3.values())
for x in d2.values():
    print(x)

#9. dicts.items() : it will return key-value pait n form if list of tuple [(k1,v1),(k2,v2)]

print(d2.items()) #return type is dict_items

for k,v in d2.items():
    print(k,'-->',v)

#10. dict1 = dict2.copy()
# Dictionary d4
d4 = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

d5 = d4.copy()
print(d4)
print(d5)

#11. dict.default(k,v) : If key is present return the value(do not update) and if key not present, add the value in dict
#d[key]=values
#d.setdefault(k,v)
# Dictionary d6
d6 = {
    "animal": "Dog",
    "breed": "Golden Retriever",
    "age": 5
}
print(d6.setdefault('animal','many-Dogs'))
print(d6.setdefault('work','Sleep'))
print(d6)

#12. d.update(x) : update one dict wit another dict, and it can be updated d.update([(k,v)])

d5.update(d6)
print(d5)

d5.update([(777,'A')])
print(d5)





