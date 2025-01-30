import numpy as np

# Array and scalar broadcasting
arr = np.array([1,2,3])
print(arr+10)

matrix = np.array([[1,2,3], [4,5,6]])
vector = np.array([1,0,1])
print(matrix + vector)

print("standard deviation", np.std(matrix))

arr = np.array([1,2,3,4,5,6])
evens = arr[arr % 2 == 0]
print(evens)

arr[arr>2] = 0
print("modified array : ", arr)