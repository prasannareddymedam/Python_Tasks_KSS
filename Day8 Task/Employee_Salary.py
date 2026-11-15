""" Write a Python program that: 
  Reads employee data from the file 
  Displays all employee details 
  Finds the employee with the highest salary 
  Appends a new employee record to the file.
"""


# Employee Salary Management System
# Reads file, display details, finds highest salary, appens new record

# Create employee.txt - Run once
with open("employee.txt", "w") as f:
    f.write("Usha 25000\n")
    f.write("Ram 30000\n")
    f.write("Asha 28000\n")

# Main Program
# To store highest salary employee name
highest_name =""
# To store highest salary
highest_salary = 0

print("--- Employee Details ---")

# Open in read mode
with open("employee.txt", "r") as f:
    # Readline by line
    for line in f:
        # Display record without extra line
        print(line.strip())

        # Split into Name and Salary->['Usha','25000']
        parts = line.split()
        # Take name
        name = parts[0]
        # Take salary, convert to int
        salary = int(parts[1])

        # Check if this salary is highest
        if salary > highest_salary:
            # Update highest salary
            highest_salary = salary
            # Update highest name
            highest_name = name

# Display name
print("\nHighest Salary Employee :", highest_name)
# Display salary
print("Salary             :",highest_salary)

# Append new employee
# 'a' Append mode, old data safe
with open("employee.txt", "a") as f:
    # Add new record
    f.write("Priya 32000\n")
    
# confirm message
print("\nNew employee Priya addded successfully!")


