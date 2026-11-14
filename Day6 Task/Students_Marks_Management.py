# Develop a Python program to manage student marks for three subjects. Store the subject 
# names in a tuple, maintain unique student names in a set, and store each student’s marks 
# in a list inside a dictionary where the key is the student name. Create user-defined 
# functions to add a student with marks, display all student records, and calculate the average 
# marks of a student. Implement a recursive function to calculate the total marks from the list of 
# marks. The program should interact with the user through a simple menu. Also include 
# exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError 
# (average calculation issues), TypeError (incorrect data type in marks), and NameError (when a 
# student name entered does not exist in the dictionary).



# Tuple to store subject names - tuple cannot be changed
subjects = ("Maths", "Science", "English")

# Set to store unique student names - set does not allow duplicates
student_names = set()

# Dictionary to store student records - key is name, value is marks list
student_records = {}

# Recursive function to calculate total marks from list
def total_marks(marks, index=0):
    # Base condition - if index reaches end of list, return 0
    if index == len(marks):
        return 0
    # Current mark + total of remaining marks (recursive call)
    return marks[index] + total_marks(marks, index + 1)

# Function to add a student with marks
def add_student():
    try:
        # Taking student name as input
        name = input("Enter student name: ")
        marks = []
        # Taking marks for each subject
        for sub in subjects:
            mark = int(input(f"Enter marks for {sub}: "))
            # Checking if mark is integer, otherwise raise TypeError
            if type(mark) != int:
                raise TypeError("Marks must be numbers")
            marks.append(mark)
        # Adding name to set
        student_names.add(name)
        # Storing name and marks list in dictionary
        student_records[name] = marks
        print("Student added successfully!")
    # If user enters non-numeric marks, this error occurs
    except ValueError:
        print("Error: Please enter numeric marks only!")
    # If marks are of wrong data type, this error occurs
    except TypeError as e:
        print("Error:", e)

# Function to display all student records
def display_students():
    # If no records are present, show message
    if len(student_records) == 0:
        print("No students found!")
        return
    # Printing each student name and marks from dictionary
    for name, marks in student_records.items():
        print(name, ":", marks)

# Function to calculate average marks of a student
def calculate_average():
    try:
        # Taking student name for average calculation
        name = input("Enter student name: ")
        # If name is not in dictionary, raise NameError
        if name not in student_records:
            raise NameError("Student not found!")
        # Getting marks list of that student
        marks = student_records[name]
        # Calculating total using recursive function
        total = total_marks(marks)
        # Average = Total / Number of subjects
        avg = total / len(marks)
        print(f"{name} Average Marks: {avg}")
    # If student name does not exist in dictionary, this error occurs
    except NameError as e:
        print("Error:", e)
    # If marks list is empty, division by zero error occurs
    except ZeroDivisionError:
        print("Error: Cannot calculate average, no marks found!")

# Main menu to interact with user
while True:
    print("\n--- Student Marks Menu ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")
    choice = input("Enter your choice: ")
    # Calling function based on user choice
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        print("Exiting... Thank You!")
        break
    else:
        print("Invalid choice! Try again.")
