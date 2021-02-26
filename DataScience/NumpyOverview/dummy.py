import numpy as np

defaultIntArray=np.array([4,6,1])
floatArray=np.array([[3,4,6],[1,2,6]],dtype=np.float32)

#print(defaultIntArray)
#print(type(defaultIntArray))

# print(floatArray)
# print(type(floatArray))
# print("default array shape: ",defaultIntArray.shape)
# print("default array stride: ",defaultIntArray.strides)
# print("float array stride: ",floatArray.strides)
# print("floatArray shape: ",floatArray.shape)

print(floatArray.shape)
print(floatArray.ndim)
