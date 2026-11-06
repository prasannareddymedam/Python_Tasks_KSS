# Write a recursive function to calculate the factorial of a number.

def f(n):
    if n==0:
        return 1
    return n*f(n-1)
print(f(5))
