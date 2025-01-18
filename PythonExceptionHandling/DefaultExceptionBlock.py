'''Default Except Block : This block is executed when an exception is raised but it is not handled by any of the except blocks. It is used to handle all the exceptions that are not handled by the specific except blocks. It is generally used to print some error message and exit the program gracefully.'''

try:
    x=int(input('Enter First Number:'))
    y=int(input('Enter Second Number:'))
    print(x/y)
except ZeroDivisionError as e:
    print(e)
except:
    print('Some Error Occurred : Default Except Block')

#NOTE : Default block should be the last block in the try-except block. If it is placed before the specific except blocks, then the specific except blocks will never be executed.