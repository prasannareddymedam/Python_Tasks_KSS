# Basic File Logger 
"""Scenario: 
   A system logs user actions. 
   Task: 
   ● Take user input 
   ● Store logs in a file 
   ● Use loop to allow multiple entries 
   ● Handle file errors using exception handling
 """

import datetime

try:
    with open("log.txt", "w") as f:
        while True:
          log = input("Enter log/exist:")
          if log == "exit":
              break
          f.write(f"{datetime.datetime.now()}-{log}\n")
    print("Logs Saved!")
except FileNotFoundError:
    print("File error!")
