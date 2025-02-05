#Inheritance Model (In -A relationhip)
# syntax:
# class childclass(parentclass)

#Example 1:
class X:
    a=10
    def m1(self):
        print('Parent class Instance Method')

class Y(X):#varable, methods constructor of parent class X will be avilable for child class
    pass

y=Y()
print(y.a)
y.m1()


'''
> print(y.a) #first prority is to child class
> If y.a avilable in child clild then it get priorty rather than parent
> It is Applicable for all the method,instance variable ,constructor and instance methods
> to resolve this super() method comper to play
'''
class Parent:
    def __init__(self):
        print('Parent Constructor')

class Child(Parent):
    def __init__(self):
        
        super().__init__()
        print('Child Constructor')

c=Child()

#output before super:Child Constructor
#output after super : Parent Constructor
                    # Child Constructor