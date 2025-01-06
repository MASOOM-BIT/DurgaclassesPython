"""A Python function is a block of reusable code that performs a specific task.
Functions allow you to encapsulate code into a single unit,
which can be called and reused multiple times throughout your program."""
#1 . Built-in functions :
#print(),len(),eval(),input(),id(),sorted().....etc.
#2. User-Defined Function
"""def function_name():
   body(logic)
   return result"""

def wish():
    print("Good Evening..")
    print("Good Evening..")
    print("Good Evening..")

wish()
wish()
wish()

#Passing parameter in python
def wish1(name):
    print("Hello",name)

wish1('Masoom')
wish1('Raza')

#giving return value
def square(num):
    return num*num

print(square(5))
print(square(10))
print(square(20))

def evenodd(num):
    if num%2==0:
        return 'Even'
    else:
        return 'Odd'

print(evenodd(24))
print(evenodd(23))


#will return None if No return statement is followed

def f1():
    print('Hello')
f1()
print(f1()) #None

