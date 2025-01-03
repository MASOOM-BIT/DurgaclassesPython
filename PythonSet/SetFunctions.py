#1.SetName.add(NewElement) : add an item to set
s1={10,20,30,40}
s1.add(50)
print(s1)

s2=set() #Empty Set
s2.add(10)
s2.add(20)
s2.add(30)
s2.add(40)
s2.add('durga') #also valid
print(s2)
#if try to add multiple items/sequence
li2=[1,2,3]
try:
    s1.add(10,20,30)
except TypeError as msg:
    print(msg)

try:
    s1.add(li2)
except TypeError as msg:
    print(msg)


#2. SetName.update(sequence) # use to extend any number of argument

li1=[50,60,70,80,90,100]
s2.update(li1)
s2.update(li1,range(1,5),'durga') #multiple sequence in argument also possib;e
print(s2)

#if try to update a single element
try:
    s2.update(10)
except TypeError as msg:
    print(msg)


#3. copy() : return separate exact copy of set
s4={10,20000,30343,4434}
s5=s4.copy()
print(s4)
print(s5)
print(id(s4))
print(id(s5))
#changes in s4 will not reflect in s5
s4.add(7948375)
print(s4)
print(s5)

# 4. pop() : To remove and return a random element
#print(s4.pop())
#print(s4.pop())
#print(s4.pop())
#print(s4.pop())
#print(s4.pop())
#print(s4.pop())
s6=set()
try:
    print(s6.pop()) #tpe error if set is empty
except KeyError as msg:
    print(msg)

#5. remove(element) : to remove a particular element

s7= {10,20,3000,4534,3242}
print(s7.remove(10)) #return None
print(s7)
try:
    print(s7.remove(999)) #KeyError is element is not found
except KeyError as msg:
    print(msg)

#6. discard(element) : if don't want any error while removing a specific element
print(s7.discard(999)) #just return None , But no Error

#7. Clear() : truncate the whole set
s8={4534,4353,True,False}
s8.clear()
print(s8) #return set() , which indicate it is empty set




