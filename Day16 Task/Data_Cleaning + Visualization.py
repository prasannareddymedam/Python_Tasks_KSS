#  Data Cleaning + Visualization 
"""Scenario: 
   data = np.array([100, np.nan, 200, 150, np.nan, 300]) 
   Task: 
   1. Convert to Pandas Series 
   2. Replace NaN with mean 
   3. Plot: 
        ○ Line graph of cleaned data 
        ○ Bar chart of values > average
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

s = pd.Series(data)
print(s)
cleaned = s.fillna(s.mean())
print("After Cleaning:\n", cleaned)
print("Mean = ", s.mean())

plt.plot(cleaned, marker = "o")
plt.title("Cleaned Data - Line Graph")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()

above_avg = cleaned[cleaned > cleaned.mean()]
print("Above Average:\n", above_avg)
plt.bar(above_avg.index, above_avg.values, color = "green")
plt.title("Vaues > Average(187.5)")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()
