#  Pie Chart with Conditional Data 
"""Scenario: 
   scores = np.array([40, 60, 80, 30, 90]) 
   Task: 
   ● Categorize into: 
       ○ Pass (>50) 
       ○ Fail (<=50) 
   ● Count using NumPy/Pandas 
   ● Plot pie chart for Pass vs Fail
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = np.array([40, 60, 80, 30, 90])

Pass_Count = np.sum(scores > 50)
Fail_Count = np.sum(scores <= 50)
print("Pass:",Pass_Count, "Fail:",Fail_Count)

plt.pie([Pass_Count,Fail_Count],labels = ["Pass(>50)","Fail(<=50)"],
        autopct = "%1.1f%%",startangle = 90)
plt.title("Pass vs Fail")
plt.show()

