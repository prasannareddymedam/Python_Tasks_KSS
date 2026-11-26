#  Employee Management System (OOP + File + Dict) 
"""Scenario: 
   Manage employee data. 
   Task: 
   ● Create a class Employee 
   ● Store employees in a dictionary 
   ● Save data to a file 
   ● Use exception handling for invalid salary input 
   ● Use loop to display all employees
"""

class Employee:
    def __init__(self, eid, name, salary):
        self.eid, self.name, self.salary = eid, name, salary
    def show(self):
        return f"{self.eid}|{self.name}|{self.salary}"
emps = {}
for _ in range(2):
        
   try:
      eid = input("ID: "); name = input("Name: ")
      salary = float(input("salary: "))
      emps[eid] = Employee(eid, name, salary)
   except ValueError:
       print("Invalid salary!")
       
open("employees.txt", "w").write("\n".join(e.show() for e in emps.values()))

for e in emps.values():
    print(e.show())
