# . Random Dataset Normalization + Filtering 
"""Scenario: 
   ● Generate 8 random float values between 0 and 1. 
   Task: 
   1. Normalize by multiplying with 100 
   2. Filter values greater than 50 
   3. Sort the filtered values
 """

import numpy as np

arr = np.random.rand(8)
print("Original:", arr)

normalized = arr*100
filtered = normalized[normalized > 50]
print("Normalized:", normalized)
print("Filter>50:", filtered)
print("Sorted:", np.sort(filtered))
 
