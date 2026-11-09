# Given a list `[1, 2, 3, 2, 4, 1, 5, 3]`, remove duplicate elements while preserving the original order. Do not use `set()`.

a = [1,2,3,2,4,1,5,3]
r =[]
for i in a:
    if i not in r:
        r.append(i)
print(r)       
    
