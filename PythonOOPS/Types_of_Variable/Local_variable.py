#sometimes to meet temporary requirements inside a method, we can declare a variable , Which will be local to that method only.
# > Local to that paticular method only

class Test:
    
    def m2(self):
        i=0 # Local variable
        while i<10:
            print('Local Variable:',i)
            i=i+1
t=Test()
t.m2()

#When Local Variable will be created?:
#When the method called then only local variable will be intiated , And as soon as method execution completes, Local variable will be destroyed.

class Test:
    def m1(self):
        x=10
        print(x)
    def m2(self):
        b=200
        print(b)
        #try:
            #print(x)
        #except NameError as msg:
            #print('Local variable x is not available in m2() method',msg)

t=Test()
t.m1()
t.m2()

