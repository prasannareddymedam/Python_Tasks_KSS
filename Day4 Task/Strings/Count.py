# Write a program to count the number of vowels in a string.

s = "Hello"
c=0
for i in s:
    if i in "aeiouAEIOU":
      c+=1
print(c)
