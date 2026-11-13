# Write a program to check whether a given number is an Armstrong number or not.

num = int(input("Enter number: "))
original = num
total = 0

while num >0:
    digit = num % 10
    total = total + digit **3
    num = num //10
if total == original:
    print(original,"is an Armstrong number")
else:
    print(original,"is Not an Armstrong number")
