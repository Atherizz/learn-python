import numpy as np

#mengubah jadi array 2D
arr = np.array([1,2,3,4,5,6,7,8,9])
reshaped = arr.reshape([3,3])
print(reshaped)
print()

#mengubah baris menjadi kolom (paling)
arr = np.array([1,2,3])
expanded = arr[:, np.newaxis]
print(expanded)
print()

a = np.array((1,2,3))
b = np.array([4,5,6])
print(a+b)
print()
print(a*b)
print()
print(a/b)

arr = np.array([4,16,25])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.median(arr))
print(np.sqrt(arr))