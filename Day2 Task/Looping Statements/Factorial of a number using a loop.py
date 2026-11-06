# Write a program to calculate the factorial of a number using a loop.

n = int(input("n: "))
f = 1
for i in range(1,n+1):
    f = f*i
    print(f)
