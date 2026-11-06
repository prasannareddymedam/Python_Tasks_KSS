# Write a recursive function to calculate the sum of digits of a number.

def f(n):
    if n==0:
        return 0
    return (n%10)+f(n//10)
print(f(123))
