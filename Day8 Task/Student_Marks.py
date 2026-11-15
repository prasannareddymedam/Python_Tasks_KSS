""" Write a Python program to: 
  Read the file 
  Display all student records 
  Calculate and display the average marks of the class
    """


 # Student Marks File Analyzer

# OPen in write mode
with open("marks.txt", "w") as f:
     # write record 1
     f. write("Usha 80\n")
     # write record 2
     f. write("Madhu 90\n")
     # write record 3
     f. write("Asha 75\n")

# Main Program - Read, Display, Average
total = 0
count = 0

print("--- Students Records ---")

 # OPen in read mode
with open("marks.txt", "r") as f:
     # Read line by line
     for line in f:
         #Display record without extra line
         print(line.split())

         # Split into Name and Marks ->['Usha','80']
         parts = line.split()
         # Take marks, convert to int
         marks = int(parts[1])

         # Add to total
         total = total + marks
         # Increase student count
         count = count + 1

# Calculate average
average = total / count

print("\nTotal Students:", count)
print("Total Marks:", total)
print("Average Marks of Class:", average)
     







