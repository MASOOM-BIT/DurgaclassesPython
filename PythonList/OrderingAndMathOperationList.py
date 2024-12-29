#1.Reverse() : To reverse element of the list
li1 = [10,20,40,50,60,600]
li1.reverse()
print(li1)

#2.sort() #condition : Homogenous elements only
li2=[30,3,555,33,45,43,55]
li2.sort() #increaring order
print(li2)
li2.sort(reverse=True) # decreasing order
print(li2)

li3=['boy','cat','apple','dog','eagle']
li3.sort()
print(li3)
li3.sort(reverse=True)
print(li3)

# '+' and '*' operation in list
li4=li2+li3
print(li4)

li5=li2*2
print(li5)
