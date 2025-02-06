'''
>>> Single Inheritence:
> the concept of inherting member of one class to another class 
> one parent class -> one child class
'''
class P:
    def m1(self):
        print('Parent Method')
class C(P): #Inherting a cingle class
    def m2(self):
        print('Child Method')

c=C()
c.m1()
c.m2()
