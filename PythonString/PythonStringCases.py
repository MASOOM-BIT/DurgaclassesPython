'''
TestString='All string methods returns new values. They do not change the original string.'

print(TestString.upper())
print(TestString.lower())
print(TestString.swapcase())
print(TestString.title())
print(TestString.capitalize())

print(TestString.startswith('All'))
print(TestString.startswith('They'))
print(TestString.endswith('.'))
print(TestString.endswith('string'))

print('Durga'.isalpha())
print('Durga7876'.isalnum())
print('Durga7876'.isalpha())
print('durga'.isdigit())
print('786786'.isdigit())
print('abc'.islower())
print('Abc'.islower())
print('abc123'.islower()) #only check alphabet present are lower or not
print('ABC'.isupper())
print('Learning Python'.istitle())
print(' '.isspace())
print('12443534'.isdigit())
print('123'.istitle())
'''

#program with combination of cases function
NewTestString = input("Enter any character to check : ")
if NewTestString.isalnum():
    print("Alpha numeric")
    if NewTestString.isalpha():
        print("Alphabet")
        if NewTestString.islower():
            print("Lower Case Alphabet")
        elif NewTestString.istitle():
            print('Title case')
        else:
            print("Upper Case Alphabet")
    else:
        print('Digit')
elif NewTestString.isspace():
    print("Its a Space character")
else:
    print('Non space Special character')

