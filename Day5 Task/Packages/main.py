
from Utilities import math_operations as m
from Utilities import string_operations as s

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("Add:", m.add(a, b))
print("Mul:", m.multiply(a, b))

string = input("Enter string: ")
print("Upper:", s.to_uppercase(string))
print("Count:", s.count_characters(string))
