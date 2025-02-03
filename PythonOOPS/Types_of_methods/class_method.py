#class methods
# @classmethods -> decorator
#def m1(cls)
    #cls.x
#call by either using classname or by using object refrence

class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print(f'{name} walks with {cls.legs}')
    
Animal.walk('Dog')
Animal.walk('cat')