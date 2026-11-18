""" A software team wants to track how long functions take to execute. Create a decorator 
that measures and prints the execution time of a function.
"""

import time
def timer(func):
    def Wrapper():
        Start = time.time()
        func()
        print("Time Taken = ",time.time()-Start)
    return Wrapper

@timer
def hello():
    print("Hello")
hello()
