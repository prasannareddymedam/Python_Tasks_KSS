# Student Score Processor 
"""Scenario: 
   A teacher stores student names and marks in a list of tuples. 
   Task: 
   ● Convert data into a dictionary 
   ● Use a loop + condition to find students scoring above 50 
   ● Use math module to calculate average 
   ● Store results in a text file
 """

import math

data = [("Asha",78),("Ram",45),("Usha",92),("Madhu",55),("Manu",38)]
d = dict(data)
above = [n for n,m in d.items() if m > 50]

avg = math.fsum(d.values())/len(d)
print(d)
print("Above 50:", above)
print("Average:", round(avg,2))
open("result.txt","w").write(f"{d}\nAbove 50:{above}\nAverage:{avg:.2f}")
