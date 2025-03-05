# Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.
# permutations are used to find all possible strings
# itertools is used to find all possible strings
import itertools
chars=['a','e','i','o','u']
def possible_strings(chars):
    from itertools import permutations
    for i in permutations(chars, len(chars)):
        print(''.join(i))

possible_strings(chars)
