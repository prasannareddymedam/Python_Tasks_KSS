# Combined Visualization Dashboard 
"""Scenario: 
   sales = np.array([100, 200, 150, 300]) 
   products = ["A", "B", "C", "D"] 
   Task: 
   ● Create DataFrame 
   ● Plot: 
        ○ Line graph (trend) 
        ○ Bar chart (comparison) 
        ○ Pie chart (distribution) 
   ● Show all in single figure (subplots)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 200, 150, 300]) 
products = ["A", "B", "C", "D"]

df = pd.DataFrame({"Product":products, "Sales":sales})
print(df)
fig,axes = plt.subplots(1,3,figsize = (12,4))

axes[0].plot(products, sales, marker = "o")
axes[0].set_title("Line-Trend")
axes[0].set_xlabel("Product")
axes[0].set_ylabel("Sales")

axes[1].bar(products, sales, color = "green")
axes[1].set_title("Bar-Comparison")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Sales")

axes[2].pie(sales, labels = products, autopct = "%1.1f%%")
axes[2].set_title("Pie-Distribution")
plt.suptitle("Combined Visualization Dashboard")
plt.tight_layout()
plt.show()
