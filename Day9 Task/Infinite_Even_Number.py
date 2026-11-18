""" Create a generator function that continuously generates even numbers starting from 
2. The program should print the first N even numbers using this generator.
"""

def even_numbers():
    n = 2
    while True:
        yield n
        n = n+2

for x in even_numbers():
    print(x)
    if x==10:
        break
