# Given the following data:
#```python
#employees = [{"name": "John", "age": 25, "salary": 30000},
#             {"name": "Alice", "age": 30, "salary": 50000},
#             {"name": "Bob", "age": 28, "salary": 40000},
#             {"name": "David", "age": 35, "salary": 60000}]
#Perform the following:

e = [{"name": "John", "age": 25, "salary": 30000},
     {"name": "Alice", "age": 30, "salary": 50000},
     {"name": "Bob", "age": 28, "salary": 40000},
     {"name": "David", "age": 35, "salary": 60000}]
h = max(e,key=lambda x:x["salary"])
print(h)
f= []
for i in e:
    if i ["salary"]>35000:
        f.append(i)
print(f)
s=0
for i in e:
    s = s+i["salary"]
    avg = s/len(e)
print(avg)
n=[]
for i in e:
        n.append(i["name"])
print(n)
