'''Normal collection objects like list, tuple, set, etc. are iterable objects.
to genrate big group of data we can use genrator
it genrate data at the run time
"yeild" keyword is used to create genrator'''

def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
    yield 'E' #it will genrate data at the run time, does not store in memory

g=mygen() #genrator object is created
print(type(g)) #<class 'generator'>
print(next(g)) #A
print(next(g)) #B
print(next(g)) #C
print(next(g)) #D
print(next(g)) #E
try:
    print(next(g))
except StopIteration:
    print('Genrator is empty')

# Note : 'next()' function is used to get the next value from the genrator

#Example 2: Genrator to Countdown

def countdown(num):
    print('Start Countdown')
    while num>0:
        yield num
        num=num-1

values=countdown(5)
for i in values:
    print(i)

#Example 3: Genrator to genrate square of numbers
def square_num(n):
    for i in range(1, n + 1):
        yield i * i

values = square_num(5)
for i in values:
    print("Square of", int(i**(1/2)), "is", i)


#Example 4: Genrator to genrate cube of numbers
def cube_num(n):
    for i in range(1,n+1):
        yield i*i*i

values=cube_num(5)
for i in values:
    print("Cube of", int(i**(1/3)), "is", i)

#Example 5: Genrator to genrate fibonacci series
def fib(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b

for i in fib(10):
    print(i ,end=' ')

print('\n') # to print in new line

#Example 6: Genrator to genrate first n numbers
def first_n(n):
    num=1
    while num<=n:
        yield num
        num=num+1

values=first_n(10)
for i in values:
    print(i,end=' ')
