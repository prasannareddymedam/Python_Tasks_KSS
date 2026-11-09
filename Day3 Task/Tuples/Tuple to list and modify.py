# Write a program to convert a tuple to a list and modify the element.

t = (10,20,30)
l = list(t)
l[1]=99
t = tuple(l)
print(t)
