#  Advanced Simulation System 
"""Scenario: 
   Simulate exam results and generate reports. 
   Task: 
   ● Generate random marks using random 
   ● Store in NumPy array 
   ● Convert to Pandas DataFrame 
   ● Use OOP to represent Student 
   ● Use conditions + loops to assign grades 
   ● Save report to file 
   ● Handle errors using try-except 
   ● Use math module for statistics
 """

import random,numpy as np, pandas as pd, math

names = ["Asha","Ram","Usha","Madhu","Manu"]
marks = np.array([random.randint(30, 100)for _ in range(5)])

class Student:
    def __init__(self, name, mark):
        self.name, self.mark = name,mark
    def grade(self):
        if self.mark >=90:
            return "A"
        elif self.mark >70:
            return "B"
        elif self.mark >50:
            return "C"
        elif self.mark >46:
            return "D"
        else:
            return "F"

try:
    grades = [Student(n,m).grade()for n,m in zip(names, marks)]
    df = pd.DataFrame({"Name":names, "Marks":marks, "Grade":grades})
    print(df)
    print("Mean:", round(math.fsum(marks)/len(marks), 2))
    print("Max:", max(marks),"Min:", min(marks))
    open("report.txt", "w").write(str(df))
except Exception as e:
    print("Error:", e)
