# Write a program to remove duplicate characters from a string.
s = "hello"
print("".join(dict.fromkeys(s)))
