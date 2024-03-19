"""Create a account class with 2 attributes -balance and 
account no Create method for debit,credit and printing 
the balance"""
class Account:
    def __init__(self,bal,acc):
        self.balance =bal
        self.account = acc
    def debit(self,amount):
        self.balance -= amount
        print(f"tk-{amount} is debit from your account")
        print(f"Your current Balance is {self.print_balance()}")
    def credit(self,amount):
        self.balance += amount
        print(f"tk-{amount} is credit from your account")
        print(f"Your current Balance is {self.print_balance()}")
    def print_balance(self):
        return self.balance

a=Account(5000,1030)
a.debit(500)
a.credit(2000)
