"""  Write a Python program that
  takes a student name as input and appends it to the file.
  Then display the contents of the file.
"""


# Student Attendance Record
name = input("Enter student name: ")

# Append mode 'a' - old data will not delete,new name added at end
with open("attendence.txt", "a") as f:
    f.write(name + "\n")

print("Attendence saved successfully!")
print("\n ---Attendence List--- ")

#read mode'r' - to display all contents
with open("attendence.txt", "r") as f:
    print(f.read())
