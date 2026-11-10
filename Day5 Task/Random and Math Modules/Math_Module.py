# Write a Python program using the math module to calculate and display the square root, floor value, and ceiling value of a number entered by the user.

import math as m

n = float(input("Enter number: "))

print(f"square root:{m.sqrt(n): }")
print(f"floor:{m.floor(n)}|ceil:{m.ceil(n): }")
print(f"power(n^2):{m.pow(n,2): }")
