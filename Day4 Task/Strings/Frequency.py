# Write a program to count the frequency of each character in a string.

s = "hello"
d={}
for i in s:
    d[i]=d.get(i,0)+1
print(d)
