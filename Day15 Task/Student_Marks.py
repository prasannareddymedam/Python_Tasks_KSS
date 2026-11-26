#  Data Analysis Tool (NumPy + Pandas) 
"""Scenario: 
   Analyze student marks. 
   Task: 
   ● Generate marks using NumPy 
   ● Convert into Pandas DataFrame 
   ● Use conditions to filter passing students 
   ● Calculate mean using math/NumPy 
   ● Use loop to print results
 """

import numpy as np, pandas as pd, math

names = ["Asha","Ram","Usha","Madhu","Manu"]
marks = np.random.randint(30,100,5)
df = pd.DataFrame({"Name":names, "Marks": marks})
print(df)
print("\n passed students:")
for _, row in df.iterrows():
    if row["Marks"] >= 40:
        print(row["Name"],row["Marks"])
print("Mean:", math.fsum(marks)/len(marks))
            
