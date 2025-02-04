import numpy as np

matrix3D = np.random.randint(0,20, size=(3,2,2))
print(matrix3D)

print("kedalaman : \n", np.sum(matrix3D, axis=0))
print("baris : \n", np.sum(matrix3D, axis=1))
print("kolom : \n", np.sum(matrix3D, axis=2))

print("max : " ,np.max(matrix3D))

np.random.seed(14)
dataset = np.random.randint(0,20, size=10)
print(dataset)

threshold = 10

dataset = np.where(dataset > threshold, 1, 0)
print(dataset)
