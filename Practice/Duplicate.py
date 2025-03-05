# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other

seq = [1,1,22,3,4,5,6,6]

def all_different(seq):
    return len(seq) == len(set(seq))

if all_different(seq):
    print("all the numbers are different")
else:
    print("Duplicate element are present")