# We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.
def stone_piles(n):
    piles = []
    current_stones = n

    while current_stones > 0:
        piles.append(current_stones)
        current_stones -= 2

    return piles[::-1]

# Input
n = int(input("Enter the number of stones in the first pile: "))

# Get the stone piles
piles = stone_piles(n)

# Output the result
print("The number of stones in each pile:", piles)
