# Write a program to check whether a number is Prime.

num = int(input("Enter number: "))
count = 0

for i in range(1, num+1):
    if num % i == 0:
        print("Factor:",i)
        count = count+1
if count == 2:
    print(num,"is a Prime number")
else:
    print(num,"is Not a Prime number")
