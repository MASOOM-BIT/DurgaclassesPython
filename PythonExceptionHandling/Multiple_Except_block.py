'''for each try block, there can be multiple except blocks.
try :
    risky code
except Exception1:
    handling code
except Exception2:
    handling code
except Exception3:
    handling code

Every exception vary error to error, so we can have multiple except block for each try block.'''

# Example 1:
try:
    x=int(input('Enter First Number:'))
    y=int(input('Enter Second Number:'))
    print(x/y)
except ZeroDivisionError:
    print('Second Number should not be zero')
except ValueError:
    print('Please provide int value only')

# NOTE : If there is two Except , PVM always check from top to bottom, if the exception is matched with the first except block then the control will be transferred to the first except block and the remaining except blocks will be ignored.

# Example 2:
def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test cases
divide(10, 2)  # Should print the result
divide(10, 0)  # Should handle division by zero
divide(10, 'a')  # Should handle invalid input type