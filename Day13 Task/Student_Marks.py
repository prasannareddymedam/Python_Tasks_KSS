#  Student Marks Analysis 
"""Given marks of 5 students in 3 subjects: 
   marks = np.array([ 
   [70, 80, 90], 
   [60, 75, 85], 
   [50, 65, 70], 
   [90, 95, 85], 
   [40, 55, 60] 
   ]) 
   Task: 
   ● Calculate total marks of each student. 
   ● Identify students whose total marks are above the class average.
 """

import numpy as np

marks = np.array([ 
   [70, 80, 90], 
   [60, 75, 85], 
   [50, 65, 70], 
   [90, 95, 85], 
   [40, 55, 60] 
   ])
total = marks.sum(axis = 1)
avg = total.mean()
above_avg = total[total > avg]

print("Total Marks of each student:", total)
print("Class Average(total):", avg)
print("Students above average:", above_avg)
 
