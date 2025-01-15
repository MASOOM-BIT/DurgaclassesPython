'''dir() fucntion is used to find out the names that are defined inside a module. 
It returns a sorted list of strings.
provides list of current module's methods and attributes.'''

x=10
y=20

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
print(dir()) 
# ['__annotations__', '__builtins__', '__cached__', '__doc__', 
# '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 
# 'sub', 'x', 'y']

# dir() function can be used to find out the names that are defined inside a module.
print()
import  moduleCreation
print(dir(moduleCreation)) 
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'div', 'floor_div', 'mod', 'mul', 'power', 'sub', 'variable_x', 'variable_y']
print()

#The special attribute __name__ is the module's name, and __file__ is the filename from which the module was loaded.
print(__name__) # __main__
print()
import module1
module1.f1() 
'''This is the imported module from another module
Executed when the module is imported
the value of __name__ is: module1'''

#Thus if called form same module then __name__ is __main__ and if called from another module then __name__ is the name of the module.