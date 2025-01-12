'''A group of functions and variables saved in a file is called a module.'''
variable_x = 888
variable_y = 999

def add(a, b):
    print("The sum of a and b is: ", a+b)
def sub(a, b):
    print("The difference of a and b is: ", a-b)
def mul(a, b):
    print("The product of a and b is: ", a*b)
def div(a, b):
    print("The division of a and b is: ", a/b)
def mod(a, b):
    print("The modulus of a and b is: ", a%b)
def power(a, b):
    print("The power of a and b is: ", a**b)
def floor_div(a, b):
    print("The floor division of a and b is: ", a//b)

#__pycache__ folder is created when we run the moduleCreation.py file.
#  It contains the bytecode of the moduleCreation.py file.