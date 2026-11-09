# Given a dictionary:
#```python
#  students = {"Rahul": 85, "Amit": 92,"Priya": 78,"Sneha": 95}
#```
#Sort the dictionary based on marks in descending order and print the top two students.


d = {"Rahul": 85, "Amit": 92,"Priya": 78,"Sneha": 95}
s = sorted(d.items(),key=lambda x:x[1],reverse=True)
print(s)
print(s[:2])
