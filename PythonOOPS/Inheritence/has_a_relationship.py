'''
>>> To use memner of one class inside another class
> for example:
class Car:
    e=Engine
> Engine class has a object defined inside car class , thus all the functionality of engine avilable to car using object refrence
> code reusebility

'''
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color

    def getinfo(self):
        print('Car Name: ',self.name)
        print('Car Model: ',self.model)
        print('Car Color: ',self.color)
        
class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    
    def empinfo(self):
        print('Emp Name :',self.ename)
        print('Emp No :',self.eno)
        print('Employee car info')
        self.car.getinfo()
c=Car("inova",'2.5z','Black')
e=Employee('Durga','101',c)
e.empinfo()
        