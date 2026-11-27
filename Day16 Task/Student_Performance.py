#  Student Performance Dashboard 
"""Scenario: 
   A school records marks of students in one subject: 
   marks = np.array([45, 67, 89, 56, 72, 91, 38]) 
   students = ["A", "B", "C", "D", "E", "F", "G"] 
   Task: 
   ● Convert to Pandas DataFrame 
   ● Plot: 
        ○ Line graph → trend of marks 
        ○ Bar chart →  student vs marks  
        ○ Pie chart → Pass (>50) vs Fail 
        ○ Histogram → distribution of marks 
        ○ Scatter plot → index vs marks
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38]) 
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({"Student":students, "Marks":marks})
print(df)
print("Pass:",np.sum(marks >50))
print("Fail:",np.sum(marks <=50))

fig,axes = plt.subplots(2,3,figsize = (12,7))
fig.delaxes(axes[1,2])

axes[0,0].plot(students, marks, marker = "o")
axes[0,0].set_title("Line-Trend of marks")

axes[0,1].plot(students, marks, color = "green")
axes[0,1].set_title("Bar - Student vs Marks")

axes[0,2].pie([5,2], labels =  ["Pass(>50)","Fail"],autopct = "%1.1f%%")
axes[0,2].set_title("Pie - Pass (>50) vs Fail ")

axes[1,0].hist(marks, bins=5, color ="orange", edgecolor = "black")
axes[1,0].set_title("Histogram - Distribution of Marks")

axes[1,1].scatter(range(len(marks)),marks, color = "red")
axes[1,1].set_title("Scatter - Index vs Marks")

plt.suptitle("Student Performance Dashboard ")
plt.tight_layout()
plt.show()


