""" Write a Python program that takes multiple items from the user and writes them into the file, with each item on a new line."""

# Grocery List Manager

# No. of items
n = int(input("How many items? "))

# Open in write mode
with open("grocery.txt", "w") as f:
    # Loop for n items
    for i in range(n):
        # Take item
        item = input(f"Enteritem {i+1}: ")
        # Write + new line
        f.write(item + "\n")

print("\nGrocery list saved!")
print("--- Grocery List ---")

# Open in read mode
with open("grocery.txt", "r") as f:
    # Display all items
    print(f.read())
