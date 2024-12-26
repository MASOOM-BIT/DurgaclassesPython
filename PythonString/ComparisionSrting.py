FirstString=input("Enter First String:")
SecondString=input("Enter Second String:")

if FirstString==SecondString:
    print("Strings are Identical")
elif FirstString<SecondString:
    print("{} is Smaller than {} string".format(FirstString,SecondString))
else:
    print('{} is Bigger than {}'.format(FirstString, SecondString))