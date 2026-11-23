# Copy vs View Behavior in Data Processing 
"""Scenario: 
   A dataset: 
   [10, 20, 30, 40] 
   Task: 
   ● Create a copy of the array. 
   ● Modify the original array. 
   ● Show that the copy does not change. 
   ● Repeat using view() and observe the difference.
 """

import numpy as np

arr = np.array([10, 20, 30, 40])

copy_arr = arr.copy()
arr[0] = 99
print("Copy:",copy_arr)
print("Original:",arr)

arr = np.array([10, 20, 30, 40])

view_arr = arr.view()
arr[0] = 99
print("View:",view_arr)
print("Original:",arr)
