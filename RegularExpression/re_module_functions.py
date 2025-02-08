# > 1.match() : we use match() function to check the given pattern at beginning of target string or not.

import re
s='ab'
m=re.match(s,'abcdefgh')
if m!=None:
    print('Match is available')
    print('At Index',m.start(),'Found Symbol',m.group())
else:
    print('Match not available')
print('-----------------------------------------')
#2:fullmatch() : To match pattern to complete string to target match
s='abcdefgh'
m=re.fullmatch(s,'abcdefgh')
if m!=None:
    print('Match is available')
    print('At Index',m.start(),'Found Symbol',m.group())
else:
    print('Match not available')

print('-----------------------------------------')
#3:Search() : We can use search to search given string into target string i.e. match object of the first occurrence otherwise none
s='aa'
m=re.search(s,'abaabaaab')
if m!=None:
    print('Match is available')
    print('At Index',m.start(),'Found Symbol',m.group())
else:
    print('Match not available')

print('-----------------------------------------')

#4:findall() : This function return a list object which contain all occurrence

m=re.findall('[0-9]','a7b9k6z')
print(m) # ['7', '9', '6']

print('-----------------------------------------')
#5:finditer() : it return iterator of match object
m=re.finditer('[0-9]','a7b9k6z')
for i in m:
    print('At Index',i.start(),'Found Symbol',i.group())


print('-----------------------------------------')
#6:sub() : substitution or replacement i.e. Please check if match is available or not in target string , if yes , Please replace it with my provided string
#syntax : re.sub(regex,replacement,target string)

m=re.sub(r'\d','#','a7b9k6z') #find digit and replace with #
print(m) # a#b#k#z
print('-----------------------------------------')

#7:subn() : no. of replacement happen then use subn instead od sub

m=re.subn(r'\d','#','a7b9k6z') #find digit and replace with #
print(type(m))
print(m)
print('The result string',m[0])
print('the number if replacement',m[1])
print('-----------------------------------------')
#7:split() : Split a given string according to any thing

m=re.split('-','10-20-30-40') #find digit and replace with #
print(m)