#  Write a Python program that generates 20 random numbers between 1 and 200 using the random module and store them in a list. 
#Then using the math module, compute and display: 
# Maximum value 
# Minimum value 
# Square root of the maximum number 
# Logarithm of the minimum number

import random as r
import math as m

numbers =[r.randint(1,200) for i in range(20)]
mx = max(numbers)
mn = min(numbers)

print("List:",numbers)
print("Max:",mx,"|Min:",mn)
print("sqrt of max:",round(m.sqrt(mx),2))
print("log of min:",round(m.log(mn),2))
