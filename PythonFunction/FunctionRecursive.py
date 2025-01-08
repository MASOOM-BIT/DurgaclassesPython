"""Call a function recursively i.e. calling function into the same function 
or A function that calls itself is known as a recursive function."""

# Example1: Factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("Factorial of 5 : ",factorial(5))
print("Factorial of 0 : ",factorial(0))

# Example2: Fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print('Fibonacci sum if 10 : ',fibonacci(10))
print('Fibonacci sum if 0 : ',fibonacci(0))
print('Fibonacci sum if 1 : ',fibonacci(1))

# Example3: Sum of natural numbers  using recursion
def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)
print('The sun of first 10 Number is' ,sum(10))
print('The sun of first 0 Number is' ,sum(0))
print('The sun of first 1 Number is' ,sum(1))
print('The sun of first 5 Number is' ,sum(5))