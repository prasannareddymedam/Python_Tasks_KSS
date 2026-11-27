# Monthly Sales Analysis 
"""Scenario: 
     sales = np.array([100, 150, 200, 180, 220, 300]) 
     months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] 
   Task: 
    ● Create DataFrame 
    ● Plot: 
        ○ Line graph → sales trend 
        ○ Bar chart → month-wise comparison 
        ○ Pie chart → contribution of each month 
        ○ Histogram → frequency of sales values 
        ○ Scatter plot → month index vs sales
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

df = pd.DataFrame({"Month":months, "Sales":sales})
print(df)

fig,axes = plt.subplots(2,3,figsize = (12,7))
fig.delaxes(axes[1,2])

axes[0,0].plot(months, sales, marker = "o")
axes[0,0].set_title("Line - Sales Trend")

axes[0,1].bar(months, sales, color = "green")
axes[0,1].set_title("Bar - Month-wise")

axes[0,2].pie(sales, labels = months,autopct = "%1.1f%%")
axes[0,2].set_title("Pie - Contribution")

axes[1,0].hist(sales, bins=5, color ="orange", edgecolor = "black")
axes[1,0].set_title("Histogram - Frequency")

axes[1,1].scatter(range(len(sales)),sales, color = "red")
axes[1,1].set_title("Scatter - Index vs Sales")

plt.suptitle("Monthly Sales Analysis Dashboard")
plt.tight_layout()
plt.show()
