# Write a Python program that removes and prints every third number from a list of numbers until the list is empty.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # Hardcoded list of numbers

while numbers:
    print(numbers.pop(2))  # Removes and prints every third number from the list
# Output: