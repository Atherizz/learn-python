import numpy as np

#  create matrix
A = np.array([[1,2,3], [4,5,6], [8,5,3]])
v = np.array([1,2,3])

# Matrix-vector multiplication
result = np.dot(A,v)
det = np.invert(result)
print("Matrix Vector Multiplication: \n", result)
print("Matrix Vector Multiplication: \n", det)