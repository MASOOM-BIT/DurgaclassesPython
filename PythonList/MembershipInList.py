# in | not in
SampleList=[10,20,30,40]
print(10 in SampleList)
print(100 in SampleList)
print(100 not in SampleList)


#Membership Example : No of Vowels in the given Word
Vowel = ['A','E','I','O','U','a','e','i','o','u']
Word = input('Enter the Word : ')
found = []
for Letter in Word:
    if Letter in Vowel:
        found.append(Letter)

print(found)
print('No of Vowels Found : ',len(found))




