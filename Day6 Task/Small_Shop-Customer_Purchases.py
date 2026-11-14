# Develop a Python program for a small shop to process customer purchases. Store product 
# names and prices in a dictionary, items added to the cart in a list, product categories in a set, 
# and product details using tuples. Create functions to display products, add items to the cart, and 
# calculate the total bill. Use a recursive function to compute the total price of all items in the cart. 
# Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError 
# (calculation errors), TypeError (wrong data types in the cart), and NameError (when a product 
# name entered by the user does not exist).



# Dictionary to store product names and prices - key is name, value is price
products = {"Pen": 10, "Notebook": 50, "Pencil": 5, "Eraser": 5}

# Set to store product categories - set does not allow duplicates
categories = {"Stationery", "Books"}

# Tuple to store product details - tuple cannot be changed
# Format is (Product Name, Category, Price)
product_details = (
    ("Pen", "Stationery", 10),
    ("Notebook", "Books", 50),
    ("Pencil", "Stationery", 5),
    ("Eraser", "Stationery", 5)
)

# List to store items added to the cart
cart = []

# Recursive function to calculate total price of items in cart
def calculate_total(cart_list, index=0):
    # Base condition - if index reaches end of list, return 0
    if index == len(cart_list):
        return 0
    # Current item price + total of remaining items (recursive call)
    return cart_list[index][1] + calculate_total(cart_list, index + 1)

# Function to display all available products
def display_products():
    # Printing product details from tuple
    print("Available Products:")
    for name, category, price in product_details:
        print(f"{name} : {price}")
    # Printing product categories from set
    print("Categories:", categories)

# Function to add an item to the cart
def add_to_cart():
    try:
        # Taking product name as input
        name = input("Enter product name: ")
        # If product is not in dictionary, raise NameError
        if name not in products:
            raise NameError("Product name not found.")
        # Taking quantity as input
        qty = int(input("Enter quantity: "))
        # Checking if quantity is integer, otherwise raise TypeError
        if type(qty) != int:
            raise TypeError("Quantity data type error.")
        # Getting price from dictionary and calculating item total
        price = products[name] * qty
        # Adding [name, total price] to cart list
        cart.append([name, price])
        print(f"{name} added to cart.")

    # If user enters non-numeric quantity, this error occurs
    except ValueError:
        print("Invalid input! Please enter numeric quantity.")
    # If product name does not exist in dictionary, this error occurs
    except NameError as e:
        print(e)
    # If quantity is of wrong data type, this error occurs
    except TypeError as e:
        print(e)

# Function to view total bill
def view_total_bill():
    try:
        # If cart is empty, raise ZeroDivisionError to show error
        if len(cart) == 0:
            raise ZeroDivisionError
        # Calculating total using recursive function
        total = calculate_total(cart)
        # Displaying items in cart
        print("Cart Items:", cart)
        print(f"Total Bill: {total}")
    # If cart is empty, division / calculation error occurs
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    # If cart contains wrong data types, this error occurs
    except TypeError:
        print("Cart data type error.")

# Main menu to interact with user
while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")
    choice = input("Enter choice: ")

    # Calling function based on user choice
    if choice == "1":
        display_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        view_total_bill()
    elif choice == "4":
        print("Exiting... Thank You!")
        break
    else:
        print("Invalid choice! Try again.")
