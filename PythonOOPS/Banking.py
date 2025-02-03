import sys


class Customer:
    '''Customer class with bank operators'''
    bankname='SBI'
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    
    def deposite(self,amount):
        self.balance=self.balance+amount
        print('After deposite the balance:',self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient balance')
            sys.exit()
        self.balance=self.balance-amount
        print('After withdraw the balance:',self.balance)

print('Welcome to',Customer.bankname)
name=input('Enter your name:')
c=Customer(name)
while True:
    print('d-Deposite\nw-Withdraw\ne-Exit')
    option = input('Choose your option:').lower()
    if option=='d':
        amount=float(input('Enter the amount to deposite:'))
        c.deposite(amount)
    elif option=='w':
        amount=float(input('Enter the amount to withdraw:'))
        c.withdraw(amount)
    elif option=='e':
        print('Thanks for banking')
        sys.exit()
    else:
        print('Choose valid option')