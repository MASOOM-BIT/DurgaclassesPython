'''Nameless function is called anonymous function. 
It is defined using lambda keyword. It can have any number of arguments 
but only one expression. 
It is used when we require a nameless function for a short period of time. 
It is also known as lambda function. 
It is defined using lambda keyword. 
It can have any number of arguments but only one expression. 
It is used when we require a nameless function for a short period of time. 
It is also known as lambda function. Syntax: lambda arguments: expression'''

#syntax : lambda arguments: expression

#normal function
def square1(x):
    return x*x
print('Via Normal Fuction : ',square1(5))

#lambda function
square2 = lambda x: x*x
print('Via Lambda Function : ',square2(5))

#Example1 "lambda function to find sum of two numbers

sum=lambda a,b:a+b
print('Sum of two numbers : ',sum(10,20))
print('Sum of two numbers : ',sum(100,200))

#Example2 : to find greater number
GreatNumber = lambda a,b,c: a if a>b and a>c else b if b>c else c
print('Greater Number : ',GreatNumber(10,20,30))
print('Greater Number : ',GreatNumber(100,200,300))

#Example3 : to find even number
EvenNumber = lambda x: x%2==0
print('Even Number : ',EvenNumber(10))
print('Even Number : ',EvenNumber(11))

#Passing function as an argument to another function'
"""1. filter() function : filter() function is used to filter the 
elements of a sequence(list,tuple,set) based on a particular condition. 
It returns a list of the elements that satisfy the condition. 
Syntax: filter(function, sequence)"""

#using filter function without lambda
def is_even(x):
    if x%2==0:
        return True
    else:
        return False

li = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(is_even,li))
print('Even Number : ',even)

#using filter function with lambda
li = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x: x%2==0,li))
print('Even Number : ',even)

odd = list(filter(lambda x: x%2!=0,li))
print('Odd Number : ',odd)

"""2. map() function : map() function is used to apply a particular operation 
to every element in a sequence(list,tuple,set). 
It returns a list of the results. Syntax: map(function, sequence)"""

#using map function without lambda
def double(x):
    return x*2
li2=[1,2,3,4,5,6,7,8,9,10]
double = list(map(double,li2))
print('Double Number : ',double)

#using map function with lambda
li2=[1,2,3,4,5,6,7,8,9,10]
double = list(map(lambda x: x*2,li2))
print('Double Number : ',double)

square = list(map(lambda x: x*x,li2))
print('Square Number : ',square)

#on multiple sequence at same time using map and lambda

li3=[1,2,3,4,5]
li4=[6,7,8,9,10]
add = list(map(lambda x,y: x+y,li3,li4))
print('Addition : ',add)
#Note : seqence should be same in both list if not then extra element will be ignored
"""3. reduce() function : reduce function to a sequence(list,set,tuple) to a single value. by 
applying a particular operation to all the elements in the sequence.
Syntax: reduce(function, sequence) ,But reduce function is not available in python 3.x 
version directly. It is available in functools module. So, first we have to 
import functools module to use reduce function."""

from functools import reduce
li5=[1,2,3,4,5]
sum = reduce(lambda x,y: x+y,li5)
print('Sum : ',sum)
#Note : reduce function will return single value not list







