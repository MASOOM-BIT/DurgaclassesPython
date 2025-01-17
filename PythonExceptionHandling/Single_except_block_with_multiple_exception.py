'''Single except block that can handle multiple exceptions
In Python, we can have a single except block that can handle multiple exceptions.
only go with this approach when we want to handle all the exceptions in the same way.

Syntax:
try:
    risky code
except (Exception1, Exception2, Exception3) as e:#tuple of exceptions
    handling code

'''
# Example 1:
try:
    x=int(input('Enter First Number:'))
    y=int(input('Enter Second Number:'))
    print(x/y)
except (ZeroDivisionError, ValueError) as e:
    print(e)

