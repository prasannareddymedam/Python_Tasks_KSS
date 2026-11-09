#  Write a function that takes a string as input and returns the number of vowels.

def count(s):
    c=0
    for i in s:
        if i in "aeiouAEIOU":
           c+=1
    return c
print(count("Hello"))
