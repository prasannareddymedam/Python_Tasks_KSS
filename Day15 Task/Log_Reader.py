#  Generator-based Log Reader 
"""Scenario: 
   A large log file needs to be processed. 
   Task: 
   ● Create a generator to read file line by line 
   ● Use loop to process logs 
   ● Use condition to filter errors 
   ● Count occurrences using a dictionary
 """
try:
    open("app.log").close()
except FileNotFoundError:
    with open("app.log", "w") as f:
        f.write("INFO User logged in\n")
        f.write("ERROR Database failed\n")
        f.write("INFO Task done\n")
        f.write("ERROR Database failed\n")
        f.write("ERROR File not found\n")
        
def read_logs():
    for line in open("app.log"):
        yield line.strip()
        
counts = {}
for log in read_logs():
    if "ERROR" in log:
        counts[log] = counts.get(log,0)+1
        
print(counts)
