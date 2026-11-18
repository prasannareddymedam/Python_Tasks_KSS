""" A school wants a program to store student details. Create a Student class with 
attributes such as name, roll number, and marks. Create objects for at least three 
students and display their details.
"""

class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(self.name, self.roll, self.marks)

s1 = Student("Usha",1,90)
s2 = Student("Ram",2,85)
s3 = Student("Asha",3,88)

s1.display()
s2.display()
s3.display()
