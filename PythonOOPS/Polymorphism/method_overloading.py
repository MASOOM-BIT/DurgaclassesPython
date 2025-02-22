#if both method have same name and different argument
#in other Language we can provide which type of argument we are providing and in python there is not possible .Thus method overloading is not possible in python
#with DEfault argument or variable number of argument

#1: Overloading with Default argument(Indirectly)
class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('The Sum:',a+b+c)
        elif a!=None and b!=None:
            print('The Sum:',a+b)
        else:
            print('Please Provide 2 or 3 arg only')

t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum()

#Overloading with variable number of argument
class Test:
    def sum(self,*n):
        total=0
        for n1 in n:
            total=total+n1
        print('The sum:',total)

t=Test()
t.sum()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10,20,30,40,50)