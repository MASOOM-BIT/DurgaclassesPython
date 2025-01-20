'''There is no guarantee of execution of every statement in try block Because if an exception occurs in the try block, the control is transferred to the except block and the statements after the exception are not executed
So, if we want to execute some statements irrespective of whether an exception occurs or not, we can use the finally block.
Syntax: 
try:
    #Statements that may raise exceptions
except:
    #Exception Handling Code
    #This block is executed when an exception is raised
finally:
    #Statements that are always executed
    #Irrespective of whether an exception occurs or not
    #cleanup code
'''

#Example 1
try:
    x=int(input('Enter First Number:'))
    y=int(input('Enter Second Number:'))
    print(x/y)
except ZeroDivisionError as e:
    print(e)
finally:
    print('Finally Block : This block is always executed')

#Note: The finally block is always executed. In case of abnormal termination of the program, the finally block is executed before the program is terminated.


'''
try:
    stmt 1
    stmt 2
    stmt 3
except: XYZ
    stmt 4
finally:
    stmt 5

stmt 6
'''
'''CASE 1: When there is no exception
Output: 1,2,3,5,6 Normal Termination'''

'''CASE 2: When an exception occurs at stmt 2 and except block match
Output: 1,4,5,6 Normal Termination'''

'''CASE 3: When an exception occurs at stmt 2 and except block does not match
Output: 1,5 Abnormal Termination'''

'''CASE 4: When an exception occurs at stmt 4
Output: 5 Abnormal Termination'''
