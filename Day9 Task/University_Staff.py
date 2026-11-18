""" A university has different staff types such as Professor, LabAssistant, and 
Administrator. All inherit from a base class Staff. Implement hierarchical inheritance 
to manage and display their information.
"""

class Staff:
    def __init__(self,name):
        self.name = name

class Professor(Staff):
    def display(self):
        print("Professor:", self.name)

class LabAssistant(Staff):
    def display(self):
        print("LabAssistant:", self.name)

class Administrator(Staff):
    def display(self):
        print("Administrator:", self.name)

Professor("Ram").display()
LabAssistant("Usha").display()
Administrator("Asha").display()
