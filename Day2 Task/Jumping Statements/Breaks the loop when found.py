# Write a program that searches for a number in a list and breaks the loop when found.

a = [1,2,3,4,5]
n = int(input("Enter search number: "))

for i in a:
    if i==n:
        print(f"Found {n}")
        break
else:
        print("Not found")
