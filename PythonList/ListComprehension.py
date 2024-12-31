#without list comprehension

li1=[]
for x in range(1,11):
    li1.append(x*x)
print(li1)

# With list comprehension

li2 = [x*x for x in range(1,11)]
print(li2)

#Condtional expression with List Comprehension

li3 = [x for x in range(1,11) if x%2==0]
print(li3)

li4 = [x*x for x in range(1,11) if x%2==0]
print(li4)

#example for list Comprehension
SampleString = 'The quick brown fox jumps over the lazy dog'
word = SampleString.split()
print(word)
ListLength = [[everyWord.upper(),len(everyWord)] for everyWord in word]
print(ListLength)