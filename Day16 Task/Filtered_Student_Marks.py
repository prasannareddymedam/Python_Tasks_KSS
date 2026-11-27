# Filtered Bar Chart 
"""Scenario: 
   marks = np.array([45, 80, 60, 30, 90]) 
   names = ["A", "B", "C", "D", "E"] 
   Task: 
   ● Convert to DataFrame 
   ● Filter students with marks > 50 
   ● Plot bar chart only for filtered students
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 80, 60, 30, 90]) 
names = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({"Name":names, "Marks":marks})
filtered = df[df["Marks"] > 50]
print(filtered)

plt.bar(filtered["Name"], filtered["Marks"], color = "teal")
plt.title("Filtered Student (Marks >50)")
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.show()
