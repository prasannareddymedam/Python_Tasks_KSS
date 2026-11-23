#  Reshape & Row Averages 
"""A dataset: 
   data = np.arange(1, 13) 
   Task: 
   ● Reshape it into a 3×4 matrix 
   ● Compute average of each row
 """

import numpy as np

data = np.arange(1, 13)
matrix = data.reshape(3, 4)
print("Matrix:")
print(matrix)
print("Row Average:", matrix.mean(axis = 1))
