#  Temperature Monitoring System 
"""Scenario: 
     temps = np.array([28, 30, 32, 35, 33, 31, 29]) 
     days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
   Task: 
    ● Create DataFrame 
    ● Plot: 
        ○ Line graph → daily temperature trend 
        ○ Bar chart → day-wise temperature 
        ○ Pie chart → proportion of high (>30) vs low temps 
        ○ Histogram → temperature frequency 
        ○ Scatter plot → day index vs temperature
 """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29]) 
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame({"Day":days, "Temp":temps})
print(df)
print("High:",np.sum(temps > 30),"Low:",np.sum(temps <= 30))

fig,axes = plt.subplots(2,3,figsize = (12,7))
fig.delaxes(axes[1,2])

axes[0,0].plot(days, temps, marker = "o")
axes[0,0].set_title("Line - Daily Temp Trend")

axes[0,1].bar(days, temps, color = "green")
axes[0,1].set_title("Bar - Day-wise Temp")

axes[0,2].pie([4, 3], labels =["High (>30)", "Low (<=30)"], autopct = "%1.1f%%")
axes[0,2].set_title("Pie - High vs Low")

axes[1,0].hist(temps, bins=5, color ="orange", edgecolor = "black")
axes[1,0].set_title("Histogram - Temp Frequency")

axes[1,1].scatter(range(len(temps)),temps, color = "red")
axes[1,1].set_title("Scatter - Day Index vs Temp")

plt.suptitle("Temperature Monitoring System")
plt.tight_layout()
plt.show()
