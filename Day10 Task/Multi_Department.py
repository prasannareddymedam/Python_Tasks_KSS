# Multi-Department Data Aggregation 
"""A company collects employee counts from two branches. 
   Branch A: 
   [[10, 20], 
   [30, 40]] 
   Branch B: 
   [[5, 15], 
   [25, 35]] 
   Scenario: 
   ● Combine the two matrices. 
   ● Calculate the total employees across all departments. 
   ● Print the combined matrix and total.
   """

import numpy as np

combined = np.array([[10,20],[30,40]])+np.array([[5,15], [25,35]])
print("Combined Matrices:")
print(combined)
print("Total:",np.sum(combined))
