# Temperature Trend Line Plot 
"""Scenario: 
   Daily temperatures: 
   temps = np.array([28, 30, 32, 31, 29]) 
   Task: 
   ● Convert into Pandas Series 
   ● Plot a line graph 
   ● Add title and grid
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 31, 29])

s = pd.Series(temps, index = {"Day1","Day2","Day3","Day4","Day5"})
print(s)

plt.plot(["Day1","Day2","Day3","Day4","Day5"], temps,marker = "o",color = "red")
plt.title("Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature (c)")
plt.grid(True)
plt.show()
