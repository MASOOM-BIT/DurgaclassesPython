'''declering a function inside another function is called nested function'''

# Example 1: Nested function
def outer_function():
    print("Outer function Executed")
    
    def inner_function():
        print("Inner function Executed")
    
    inner_function()
outer_function()

#Example 2: Returning function from another function
def outer_function(outer_arg):
    def inner_function(inner_arg):
        return inner_arg * 2
    
    result = inner_function(outer_arg)
    return result + 5

# Example usage
print(outer_function(10))  # Output: 25

#Example 3: The Sum and Avrage of two numbers using nested function
def sum_avg(a,b):
    def sum(a,b):
        return a+b
    def avg(a,b):
        return (a+b)/2
    print('Sum of two numbers : ',sum(a,b))
    print('Average of two numbers : ',avg(a,b))
    print('Sum of two numbers : ',sum(a,b))
    print('Average of two numbers : ',avg(a,b))#calling as many as time we need
    print('Sum of two numbers : ',sum(a,b))
    print('Average of two numbers : ',avg(a,b)) #we now call the nested function only by call ing outer function

sum_avg(10,20)
sum_avg(100,200)

#Note : Calling inner function from outside of outer function is not possible and 
#will raise an error

#------------------------------------------------------------------------------------------

def outer():
    print("Outer Started")
    def inner():
        print("Inner Executed")
    print("Outer Function returning Inner function")
    return inner

#return inner : will return ineer as a function object
#return inner() : will return to f1() value present in inner function

f1=outer() #pointer to inner function is returned
#fuction is going to execute but returned value going to assign to f1
f1()#inner function is called from outer function

