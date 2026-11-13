# Write a program to check whether a number is a Perfect number.

num = int(input("Enter number: "))
total = 0

for i in range(1, num):
    if num % i == 0:
        print("Divisor:",i)
        total = total+i
if total == num:
    print(num,"is a Perfect number")
else:
    print(num,"is Not a Perfect number")
