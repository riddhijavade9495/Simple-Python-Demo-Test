import numpy as np

a = np.array([10,20,30,40,50])
print(a[0:3])

arr = np.array([[10,20,30,40,50],[10,20,30,40,50],[10,20,30,40,50]])
print(arr[0,1:3])
print(arr[1,2:3])
print(arr[2,0:1])
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))
print(arr.dtype)
print(arr.astype(float))
