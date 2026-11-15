"""  Write a program that opens the file, reads all the contents, and displays them on the screen."""

# Notes Reader Program

# Create File - Run once
# Open in write mode
with open("notes.txt", "w") as f:
    # Write line 1
    f.write("Today I learned File Handling\n")
    # Write line 2
    f.write("Python is easy\n")
    # Write line 3
    f.write("Practice daily\n")

# Main Program - Open, Read, Display
try:
    # Open in read mode
   with open("notes.txt", "r") as f:
       # Read full file
       data = f.read()
       print("--- Your Notes ---")
       # Display contents
       print(data)
 # If file not exists      
except FileNotFoundError:
    # Show message, no crash
    print("File not found!")
