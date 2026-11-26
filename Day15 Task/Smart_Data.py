#  Smart Data Processing Pipeline 
"""Scenario: 
   A system processes numeric data from file. 
   Task: 
   ● Read numbers from a file 
   ● Use NumPy for calculations (mean, std) 
   ● Convert results to Pandas DataFrame 
   ● Use exception handling for bad data 
   ● Use a generator to stream data 
   ● Apply decorator to measure execution time
 """

import numpy as np, pandas as pd, time, os

if not os.path.exists("numbers.txt"):
    open("numbers.txt", "w").write("10\n20\nabc\n30\n40\nbad\n50\n")
                                   
def gen():
    for line in open("numbers.txt"):
        try:
            yield float(line)
        except ValueError:
            print("Skipped:", line.strip())

def timer(func):
    def wrapper():
        s = time.time()
        r = func()
        print(f"Time:{time.time()-s:.3f}sec")
        return r
    return wrapper

@timer
def run():
    a = np.array(list(gen()))
    print("Mean:", a.mean(), "std:", round(a.std(), 2))
    print(pd.DataFrame({"Numbers": a}))

run()
