# Exception : Somewhere in programming there is always possibility of error. When error occurs, Python generates an exception that can be handled, which avoids your program to crash.
# that means , if something goes wrong at runtime there is an alternate solution to handle the error and continue the execution of the program. This is called Exception Handling.
#------------------------------------------------------------------------------------
'''
Types of Errors:
1. Syntax Error: It is also known as parsing error. It occurs when the syntax of the code is not correct. It is detected by the interpreter. 

2.Runtime Error: It is also known as an exception. It occurs during the execution of the program. It is detected by the interpreter.
------------------------------------------------------------------------------------
Some common exceptions are:
1. ZeroDivisionError: It occurs when you try to divide a number by zero.
2. NameError: It occurs when a variable is not defined.
3. TypeError: It occurs when you try to perform an operation on a data type that is not supported.
4. ValueError: It occurs when you try to perform an operation on a value that is not supported.
5. IndexError: It occurs when you try to access an index that is not available.
6. KeyError: It occurs when you try to access a key that is not available.
7. FileNotFoundError: It occurs when you try to access a file that is not available.
8. ImportError: It occurs when you try to import a module that is not available.
9. MemoryError: It occurs when a program runs out of memory.
10. KeyboardInterrupt: It occurs when the user interrupts the execution of the program.
11. EOFError: It occurs when the end of the file is reached.
12. IndentationError: It occurs when the indentation of the code is not correct.
13. AttributeError: It occurs when a class does not have an attribute.
------------------------------------------------------------------------------------
Exception Handling:Solving the problem of runtime errors is called exception handling. It is done using the try, except, else, and finally blocks.'''
#------------------------------------------------------------------------------------
'''
Defalut Exception Handling:Every exception in Python is an object. The exception class is a subclass of the BaseException class. The BaseException class is the parent class of all exceptions in Python. The BaseException class is a subclass of the object class.
Any exception happen ,PVM will create an object of that exception class and raise it. If the exception is not handled, the program will terminate abruptly and the exception object will be printed on the console.'''
#------------------------------------------------------------------------------------
#The try block is used to write the code that may raise an exception. The except block is used to handle the exception. The else block is used to write the code that will execute if the try block does not raise an exception. The finally block is used to write the code that will execute whether the try block raises an exception or not.
#------------------------------------------------------------------------------------
#Example 1: Simple program to demonstrate exception handling.

print('Start of the program')
try:
    print(10/0)  # It will raise an exception.
except ZeroDivisionError as msg:
    print('Exception:',msg)
    print(10/2)  # It will execute.
print('End of the program')

#As we Know , BaseException is the parent class of all exceptions in Python. So, we can use BaseException class to handle all exceptions in Python.

print('Start of the program')
try:
    print(10/0)  # It will raise an exception.
except BaseException as msg:
    print('Exception:',msg)
    print(10/2)
print('End of the program')
