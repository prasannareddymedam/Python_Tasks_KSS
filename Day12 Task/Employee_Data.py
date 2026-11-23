#  Employee Data Copy Issue (Shallow vs Deep Copy) 
"""A company stores employee data: 
   employees = [[101, "A"], [102, "B"], [103, "C"]] 
   Scenario: 
   ● Create a shallow copy of the list. 
   ● Modify one nested list (e.g., change "A" to "Z"). 
   ● Observe changes in both lists. 
   Task: 
   ● Explain why the change reflects in both. 
   ● Fix it using deep copy.
 """

import copy
employees = [[101, "A"], [102, "B"], [103, "C"]]

shallow = employees.copy()
shallow[0][1] = "Z"
print("shallow:", shallow)
print("Original:", employees)
print("Both changed because shallow copy shares nested lists")
print()

employees = [[101, "A"], [102, "B"], [103, "C"]]
deep = copy.deepcopy(employees)
deep[0][1] = "Z"
print("Deep:", deep)
print("Original:", employees)


