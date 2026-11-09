# Create a dictionary containing student names and marks. Add a new student, update an existing student's marks, and print all student details.

s = {"Usha":85,"Ram":80}

#Add a new student
s["Madhu"]=90

#Update existing students  marks
s["Usha"]=87
print(s)

#Print all student details
for names,marks in s.items():
     print(names,":",marks)
