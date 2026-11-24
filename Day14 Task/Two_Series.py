#  Data Alignment Issue in Series Addition 
"""Two Series: 
   S1 = pd.Series([10, 20, 30], index=["a", "b", "c"]) 
   S2 = pd.Series([5, 15, 25], index=["b", "c", "d"]) 
   Task: 
   ● Add both Series 
   ● Explain why some values become NaN 
   ● Replace NaN with 0 and compute final result
 """

import pandas as pd

S1 = pd.Series([10, 20, 30], index=["a", "b", "c"]) 
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
print("Add:")
print(S1+S2)
print("Fill NaN with 0:")
print((S1+S2).fillna(0))
print("Correct method - add with fill_value:")
print(S1.add(S2, fill_value = 0))
