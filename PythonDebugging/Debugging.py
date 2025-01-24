'''
> Mismatch between excepted result and original result
> process of identifiying and fixing a Bug is called Debugging
'''
#dugugging using print statments
#  > We use print statement to perform debugging

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        print(f"Current number: {num}")  # Debugging statement
        total += num
        print(f"Total so far: {total}")  # Debugging statement
    return total

numbers_list = [1, 2, 3, 4, 5]
result = calculate_sum(numbers_list)
print(f"The final sum is: {result}")  # Final output
