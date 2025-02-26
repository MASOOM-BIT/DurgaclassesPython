#by default all the variables are public in python
#to make a variable private we need to use double underscore(__) before the variable name
#to make a variable protected we need to use single underscore(_) before the variable name
#x=10 -> public variable
#__x=10 -> private variable
#_x=10 -> protected variable

#public Variable Example
class Test:
    def __init__(self):
        self.x=10
t=Test()
print(t.x)

#private Variable Example
class Test1:
    def __init__(self):
        self.__x=10
t1=Test1()
#print(t1.x) #this will give error because x is private variable
#print(t1.__x) #this will give error because x is private variable
print(t1._Test1__x) #this is the way to access private variable

#protected Variable Example
class Test2:
    def __init__(self):
        self._x=10
t2=Test2()
print(t2._x)

