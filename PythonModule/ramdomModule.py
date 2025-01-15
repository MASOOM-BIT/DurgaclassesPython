'''random module provides a number of functions that can be used to generate random numbers. for Example: dice rolling,OTP generation, captcha generation, password generation etc.
random(), seed(), getstate(), setstate(), getrandbits(), uniform(), randrange(), randint(), choice(), shuffle(), sample() etc.'''

# 1. random(): This function is used to generate a random float number between 0.0(inclusive) to 1.0 (Exclusive).

from random import random
for i in range(5):
    print(random(),end=' | ')
print('\n')
# 2. randint(x,y): This function is used to generate a random integer number between the given range(both range is inclusive).

from random import randint
for i in range(5):
    print(randint(10,20),end=' | ')   # It will generate a random number between 10 to 20.
print('\n')
for i in range(5):
    print(randint(1,100),end=' | ')     # It will generate a random number between 1 to 100.
print('\n')
#NOTE :randint(x,y) alwyas generate a random number between the given range(both range is inclusive). both range should be integer and cumplusory.

# 3. randrange(x,y,z): This function is used to generate a random integer number between the given range(both range is inclusive) with a step value.
'''
randrange(10) : It will generate a random number between 0 to 9.
randrange(1,11) : It will generate a random number between 1 to 10.
randrange(1,11,2) : It will generate a random number between 1 to 10 with a step value of 2.'''

from random import randrange
for i in range(5):
    print(randrange(10),end=' | ')

print('\n')

for i in range(5):
    print(randrange(1,11),end=' | ')
print('\n')

for i in range(5):
    print(randrange(1,11,2),end=' | ')

print('\n')
# 4. uniform(x,y): This function is used to generate a random float number between the given range(both range is inclusive).

from random import uniform
for i in range(5):
    print(uniform(10,20),end=' | ')   # It will generate a random number between 10 to 20.
print('\n')

# 5. choice(sequence): This function is used to generate a random element from the given any indexable sequence.

from random import choice
for i in range(5):
    print(choice('hello'),end=' | ')   # It will generate a random element from the given sequence.
print('\n')
Sample_list = [10,20,30,40,50]
for i in range(5):
    print(choice(Sample_list),end=' | ')   # It will generate a random element from the given sequence.
print('\n')
#------------------------------------------------------------------------------------

# 6. shuffle(sequence): This function is used to shuffle the given sequence.

from random import shuffle
Sample_list = [10,20,30,40,50]
shuffle(Sample_list)  # It will shuffle the given list.
print(Sample_list)

#Example 1 : Write a program to generate a random number between 1 to 6 to simulate a dice rolling.
from random import randint
print(randint(1,6))

#Example 2 : Write a program to generate a random 6 digit OTP.
from random import randint
OTP = ''
for i in range(6):
    OTP += str(randint(0,9))
print(OTP)
print()
#OR
from random import randint
for i in range(6):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')
print()
#Example 3 : Write a program to generate a random 6 digit passWord.(Password should be alphanumeric)
from random import randint
for i in range(6):
    print(chr(randint(65,90)),chr(randint(65,90)),randint(0,9),randint(0,9),chr(randint(97,122)),chr(randint(97,122)),sep='')