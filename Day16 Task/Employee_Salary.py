#  Employee Salary Insights 
"""Scenario: 
     salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
     departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"] 
   Task: 
    ● Convert into DataFrame 
    ● Plot: 
       ○ Line graph → salary trend 
       ○ Bar chart → department-wise salary comparison 
       ○ Pie chart → department distribution 
       ○ Histogram → salary distribution 
       ○ Scatter plot → index vs salary
 """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"] 


df = pd.DataFrame({"Department":departments, "Salary":salaries})
print(df)
print(df.groupby("Department")["Salary"].mean())

fig,axes = plt.subplots(2,3,figsize = (12,7))
fig.delaxes(axes[1,2])

axes[0,0].plot(departments, salaries, marker= "o")
axes[0,0].set_title("Line - Salary Trend")

avg = df.groupby("Department")["Salary"].mean()
axes[0,1].bar(avg.index, avg.values, color = "green")
axes[0,1].set_title("Bar - Dept-wise Avg Salary")

counts = df["Department"].value_counts()
axes[0,2].pie(counts.values, labels = counts.index,autopct = "%1.1f%%")
axes[0,2].set_title("Pie - Dept Distribution")

axes[1,0].hist(salaries, bins=4, color ="orange", edgecolor = "black")
axes[1,0].set_title("Histogram - Salary Distribution")

axes[1,1].scatter(range(len(salaries)),salaries, color = "red")
axes[1,1].set_title("Scatter - Index vs Salary")

plt.suptitle("Employee Salary Insights")
plt.tight_layout()
plt.show()
