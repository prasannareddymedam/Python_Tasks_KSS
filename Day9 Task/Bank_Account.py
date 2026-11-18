""" A bank wants to manage customer accounts. Create a BankAccount class with a 
constructor to initialize account number and balance. Implement methods to deposit, 
withdraw, and display balance.
"""

class BankAccount:
    def __init__(self,acc,bal):
      self.acc = acc
      self.bal = bal

    def deposit(self,amt):
        self.bal = self.bal+amt

    def withdraw(self,amt):
        self.bal = self.bal-amt

    def display(self):
        print(self.acc,self.bal)

a1 = BankAccount(12345, 1000)
a1.deposit(500)
a1.withdraw(200)
a1.display()
