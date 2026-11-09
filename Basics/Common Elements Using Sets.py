#Given two lists:
#list1 = [1, 2, 3, 4, 5]
#list2 = [3, 4, 5, 6, 7]
#Find
#Common elements
#Elements present only in the first list
#All unique elements from both lists

a1 = [1,2,3,4,5]
a2 = [3,4,5,6,7]
print(set(a1)&set(a2))
print(set(a1)-set(a2))
print(set(a1)|set(a2))
