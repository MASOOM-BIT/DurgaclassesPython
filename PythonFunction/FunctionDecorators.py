'''taking a function as input and returning a function as output , 
extending functionality of a function without modifying the origninal function 
it is called function decorator'''
#Example 1: Simple Decorator

def decorator_function(func):
    def wrapper(name):
        if name == "Sunny":
            print("Hello Decor Sunny")
        else:
            func(name)
    return wrapper
@decorator_function
def greet(name):
    print("Hello",name)

greet("Durga")
greet("Ravi")
greet("Sunny")
decoreFunction = decorator_function(greet)
decoreFunction("Durga")


#Example 2: Decorator with arguments
def smartdivision(func):
    def inner(a,b):
        if b==0:
            print("Division is not possible")
            return
        else:
            return func(a,b)
    return inner
@smartdivision
def division(a,b):
    return a/b

print(division(10,2))
print(division(10,0))

#Example 3: Chaining Decorators in Python
def decor1(func):
    def inner():
        x = func()
        return x*x
    return inner
def decor2(func):
    def inner():
        x = func()
        return 2*x
    return inner
@decor1
@decor2
def num():
    return 10
print(num())
#The decorators are applied in a nested manner. 
# First, decor2 is applied to num, 
# then decor1 is applied to the result of decor2(num).

