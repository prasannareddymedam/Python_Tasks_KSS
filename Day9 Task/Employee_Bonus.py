""" A company wants to apply a bonus calculation automatically before displaying the 
salary. Create an Employee class and use a decorator that modifies the salary by 
adding a bonus before displaying it.
"""

def add_bonus(func):
    def Wrapper(self):
        self.salary = self.salary +5000
        func(self)
    return Wrapper

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @add_bonus
    def display(self):
        print(self.name,self.salary)

e1 = Employee("Usha",30000)
e1.display()
