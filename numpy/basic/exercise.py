import numpy as np

a = np.arange(1,6)
b = np.arange(6,11)

print(a)
print(b)

print("Tambah: ", a + b)
print("Kurang: ", a - b)
print("Kali: ", a * b)
print("Bagi: ", a / b)

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
transpose = matrix.T
print(matrix)
print(transpose)

matrix2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
matrix2D = matrix2.reshape(4,4)
print(matrix2D)

baris = np.sum(matrix2D, axis=1)
kolom = np.sum(matrix2D, axis=0)
print(baris)
print(kolom)
print(np.min(matrix2))
