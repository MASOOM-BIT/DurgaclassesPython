"""Four type of arguments in Python function:
1. Positional arguments
2. Keyword arguments
3. Default arguments
4. Variable-length arguments
"""
#1. Positional arguments: passed in correct positional order

def add(a,b):
    return a+b  #return the sum of two numbers  a and b
print(add(10,20))  #Output: 30 #Here, 10 is assigned to a and 20 is assigned to b based on the order of arguments  a and b

#will get TypeError: add() missing 2 required positional arguments: 'a' and 'b'
try:
    print(add(50,100,200))
except TypeError as e:
    print(e)
#2. Keyword arguments: passed with the key-value syntax #order of arguments doesn't matter
def sub(a,b):
    return a-b  #return the difference of two numbers  a and b
print(sub(a=100,b=50))  #Output: 50 #Here, 100 is assigned to a and 50 is assigned to b based on the key

#Passing positional arguments and keyword arguments together
# Rule: positional arguments should be passed before keyword arguments
def mul(a,b,c):
    return a*b*c  #return the product of three numbers  a, b and c
print(mul(10,20,c=30))  #Output: 600 #Here, 10 is assigned to a, 20 is assigned to b and 30 is assigned to c based on the order of arguments  a, b and c

#Will give syntax error: positional argument follows keyword argument if we pass positional argument after keyword argument

#3. Default arguments: default value is assigned to the argument if the value is not passed during the function call
def div(a,b=2):
    return a/b  #return the division of two numbers  a and b #here, b is assigned default value 2
print(div(10))  #Output: 5 #Here, 10 is assigned to a and b is assigned default value 2 as it is not passed during the function call
print(div(10,5))  #Output: 2 #Here, 10 is assigned to a and 5 is assigned to

# SyntaxError: non-default argument follows default argument if we pass non-default argument after default argument in the function call
#default argument should be last argument in the function definition

#4. Variable-length arguments: *args and **kwargs
#defnition : def function_name(*args, **kwargs):    #*args is used to pass variable number of non-keyword arguments and **kwargs is used to pass variable number of keyword arguments       

def sum(*args):
    result=0
    for x in args:
        result=result+x
    return result
print('the Sum :',sum(10,20,30))  #Output: 60 #Here, 10, 20 and 30 are passed as arguments and stored in args as tuple
print('the Sum :',sum(10,20,30,40,50))  #Output: 150 #Here, 10, 20, 30, 40 and 50 are passed as arguments and stored in args as tuple

def display(**kwargs):
    for key, value in kwargs.items():
        print(key,"--->", value)
display(name='John', age=25, city='New York')  #Output: name John, age 25, city New York #Here, name, age and city are passed as keyword arguments and stored in kwargs as dictionary
print()
display(name='Smith', age=30, city='Los Angeles', country='USA')  #Output: name Smith, age 30, city Los Angeles, country USA #Here, name, age, city and country are passed as keyword arguments and stored in kwargs as dictionary

#using variable-length arguments with other arguments
def details(name, *args, **kwargs):
    print('Name:',name)
    print('Positional arguments:',args)
    print('Keyword arguments:',kwargs)

details('John', 25, 'New York', age=25, city='New York')  #Output: Name: John, Positional arguments: (25, 'New York'), Keyword arguments: {'age': 25, 'city': 'New York'}   #Here, name, age and city are passed as positional arguments and stored in args as tuple and age and city are passed as keyword arguments and stored in kwargs as dictionary    
print()
details('Smith', 30, 'Los Angeles', age=30, city='Los Angeles', country='USA')  #Output: Name: Smith, Positional arguments: (30, 'Los Angeles'), Keyword arguments: {'age': 30, 'city': 'Los Angeles', 'country': 'USA'}   #Here, name, age and city are passed as positional arguments and stored in args as tuple and age, city and country are passed as keyword arguments and stored in kwargs as dictionary    
