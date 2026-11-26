#  Random Number Analyzer 
"""Scenario: 
   A system generates random numbers for testing. 
   Task: 
   ● Use random to generate 10 numbers 
   ● Store in a list 
   ● Use loop + condition to count even/odd numbers 
   ● Use set to remove duplicates
 """

import random

nums = [random.randint(1, 100) for _ in range(10)]

even = odd = 0
for n in nums:
    if n%2 == 0:even += 1
    else: odd += 1
print(nums)
print("Even:", even,"Odd:", odd)
print("Unique:", set(nums))
