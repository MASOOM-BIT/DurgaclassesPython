class Account:
    def __init__(self,name,balance,min_balance) -> None:
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
            self.balance-=amount
        else:
            print('Insufficient Balance')

    def print_statement(self):
        print('Account Balance :',self.balance)

class Current(Account):
    def __init__(self,name,balance) -> None:
        super().__init__(name,balance,min_balance=1000)

    def __str__(self) -> str:
        return f'Account Name: {self.name} and Balance: {self.balance}'

class Savings(Account):
    def __init__(self,name,balance) -> None:
        super().__init__(name,balance,min_balance=0)
    
    def __str__(self) -> str:
        return f'Account Name: {self.name} and Balance: {self.balance}'
    



if __name__ == '__main__':
    c=Savings('Durga',10000)
    print(c)
    c.deposit(5000)
    c.print_statement()
    c.withdraw(15000)
    c.print_statement()
    c.withdraw(15000)
    c.print_statement()

    c1=Current('Ravi',10000)
    print(c1)
    c1.deposit(5000)
    c2=Current('israfil',100)
    print(c2)
    c2.deposit(1000)
    c2.print_statement()
