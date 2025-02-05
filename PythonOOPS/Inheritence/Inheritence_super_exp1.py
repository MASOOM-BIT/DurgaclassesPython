class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat_and_drink(self):
        print('Briyani and coke')

class softEn(Person):
    def __init__(self, name, age,eno,esal):
        super().__init__(name, age)
        self.eno=eno
        self.esal=esal
    
    def work(self):
        print('coding')

s=softEn('Durga',48,101,100000)
s.eat_and_drink()
s.work()