""" A company has two types of employees: Employee and Manager. Create a base class 
Employee containing name and salary. Create a derived class Manager that inherits 
from Employee and displays the employee details.
"""

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def display(self):
        print(self.name,self.salary)

m1 = Manager("Ramesh", 50000)
m1.display()
