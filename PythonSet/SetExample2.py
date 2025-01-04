#diffrent vowels in given string
SampleString = input("Enter String : ")
vowels = ['A','E','I','O','U','a','e','i','o','u']
Set1 = set(SampleString)
Vol = Set1.intersection(vowels)
print(Vol)
print("No of Vowels : ",len(Vol))