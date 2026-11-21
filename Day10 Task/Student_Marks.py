# Student Marks Analysis
"""A teacher stores the marks of 5 students in a NumPy array. 
   Scenario: 
   You are given marks [45, 67, 89, 56, 72]. 
   Task: 
   ● Convert the list into a NumPy array. 
   ● Add 5 grace marks to every student. 
   ● Print the updated marks.
   """

import numpy as np

marks = [45,67,89,56,72]
arr = np.array(marks)
updated_marks = arr + 5
print ("Updated Marks:", updated_marks)
