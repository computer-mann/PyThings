import numpy as np


a = np.array([[9,2], [3,4], [5,6]])
(x,y) = a.max(axis=0)

print(x,y)