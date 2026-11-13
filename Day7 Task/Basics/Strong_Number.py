# Write a program to check whether a given number is a Strong number.

import math

num = int(input("Enter number: "))
original = num
total = 0

while num >0:
    digit = num % 10
    total = total + math.factorial (digit)
    num = num //10
if total == original:
    print(original,"is a Strong number")
else:
    print(original,"is Not a Strong number")
