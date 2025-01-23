def sum_of_digit(num):
    sumofdigit = 0  # Initialize sum outside the loop
    while num > 0:
        sumofdigit += num % 10  # Add the last digit of num to the sum
        num = num // 10  # Remove the last digit from num
    return sumofdigit

print(sum_of_digit(43))  # Output: 7
