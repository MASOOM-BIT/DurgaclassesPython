#SamleProgram for diffrent control flow of try except block
try:
    print(10/2) #stmt 1
    print(10/0) # It will raise an exception. #stmt 2
    print(10/5) # It will not execute. #stmt 3
except TypeError as msg:
    print('Exception:',msg)
    print(10/5)  # It will #stmt 4
print('End of the program') #stmt 5

'''
Case 1: If there is no exception in the try block.
Output: 5.0
3.3333333333333335
2.0
End of the program'''

'''
CASE 2 :If an Exception is raised at expression 2 and except block is matched with the 
exception
output : stmt 1 , 4, 5 will Execute stmt 3 will not be Executed
Note : stmt 3 will not be executed because the exception is raised at stmt 2 and the control is transferred to the except block.'''

'''
Case 3: If an Exception is raised at expression 2 and except block is not matched with the exception.
Output: stmt 1 will execute the program will terminate abruptly and the exception object will be printed on the console.
'''

'''
Case 4: If an Exception is raised at stmt 4
Output: Abnormal Terminated and the exception object will be printed on the console.'''
