# Given a string `"programming"`, create a dictionary that counts how many times each character appears.

s = "programming"
d ={}
for c in s:
    if c in d:
        d[c]=d[c]+1
        
    else:
        d[c]=1
print(d)
