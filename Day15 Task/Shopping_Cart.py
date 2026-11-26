#  Shopping Cart System 
"""Scenario: A user adds items to a shopping cart. 
   Task: 
   ● Store items in a list 
   ● Convert to set to remove duplicates 
   ● Use loop + condition to calculate total cost 
   ● Handle invalid input using try-except
 """

items = [("Milk",40),("Sugar",30),("Milk",40),("Eggs",50)]
print("Items:", items)
print("Unique Items:", set([i for i, _ in items]))

total = 0
for _, price in items:
    total += price
print("Total cost:", total)
try:
    qty = int(input("Enter quantity:"))
    print("Bill:", total*qty)
except ValueError:
    print("Invalid input! Enter number only.")
