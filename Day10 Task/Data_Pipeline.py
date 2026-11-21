#  Data Processing Pipeline 
"""A data pipeline receives the following array: 
   [12, 7, 25, 3, 18, 10] 
   Scenario: 
   1. Convert the list into a NumPy array. 
   2. Sort the array. 
   3. Split the sorted array into two equal parts. 
   4. Calculate the sum of each part. 
   Output: 
   ● Sorted array 
   ● Two split arrays 
   ● Sum of each part
   """

import numpy as np

arr = np.sort(np.array([12,7,25,3,18,10]))
p1,p2 = np.split(arr,2)
print("Sorted:", arr)
print("part1:", p1,"sum:", np.sum(p1))
print("part2:", p2,"sum:", np.sum(p2))
