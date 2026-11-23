#  Random Data & Filtering 
"""Generate random numbers: 
   nums = np.random.randint(1, 100, 10) 
   Task: 
   ● Filter values that are divisible by 5 
   ● Return sorted result.
 """

import numpy as np

np.random.seed(0)
nums = np.random.randint(1, 100, 10)
filtered = nums[nums%5 == 0]
sorted_result = np.sort(filtered)
print("Origal:", nums)
print("Divisible by 5:", filtered)
print("Sorted:", sorted_result)
 
