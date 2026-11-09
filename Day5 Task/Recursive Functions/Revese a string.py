# Write a recursive function to reverse a string.

def f(s):
    if len(s)<=1:
        return s
    return f(s[1:])+s[0]
print(f("hello"))
