#factorial : 5! = 5*4*3*2*1
def fact(num):
    result = 1
    while num>=1:
        result = result * num
        num=num-1
    return result

print(fact(9))

for i in range(1,10):
    print('Factorial of {} is : {}'.format(i,fact(i)))


