#  Product Sales & Profit Analysis 
"""Scenario: 
     sales = np.array([200, 300, 250, 400, 350]) 
     profit = np.array([50, 70, 60, 90, 80]) 
     products = ["A", "B", "C", "D", "E"] 
   Task: 
    ● Create DataFrame 
    ● Plot: 
       ○ Line graph → sales trend 
       ○ Bar chart → product vs sales 
       ○ Pie chart → sales contribution 
       ○ Histogram → profit distribution 
       ○ Scatter plot → sales vs profit
 """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350]) 
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]
     
df = pd.DataFrame({"Product":products, "Sales":sales, "Profit":profit})
print(df)

fig,axes = plt.subplots(2,3,figsize = (12,7))
fig.delaxes(axes[1,2])

axes[0,0].plot(products, sales, marker = "o")
axes[0,0].set_title("Line - Sales Trend")

axes[0,1].bar(products, sales, color = "green")
axes[0,1].set_title("Bar - Product vs Sales")

axes[0,2].pie(sales, labels = products,autopct = "%1.1f%%")
axes[0,2].set_title("Pie - Sales Contribution")

axes[1,0].hist(sales, bins=4, color ="orange", edgecolor = "black")
axes[1,0].set_title("Histogram - Profit Distribution")

axes[1,1].scatter(sales, profit, color = "red")
axes[1,1].set_title("Scatter - Sales vs Profit")
axes[1,1].set_xlabel("Sales")
axes[1,1].set_ylabel("Profit")

plt.suptitle("Product Sales & Profit Analysis")
plt.tight_layout()
plt.show()

