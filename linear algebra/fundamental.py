import numpy as np

A = np.array([[1,2], [3,4]])
B = np.array([[4,3], [5,2]])

print("Penjumlahan : \n", A + B)
print("Pengurangan : \n", A - B)

# Perkalian
print("Perkalian : \n", np.dot(A,B))

# Matrix identitas
print("Matrix identitas : \n", np.eye(3))

# Matrix zero
print("Zero : \n", np.zeros((2,3)))

D = np.diag([1,2,3])
print("Diagonal Matrix \n", D)
