import numpy as np

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
vector = np.array([1,0,-1])

result_add = matrix + vector
print("Add: \n", result_add)

result_mul = matrix * 2
print("Multiplication: \n", result_mul)

dataset = np.random.randint(1,51, size=(5,5))
dataset[dataset > 25] = 0

print("jumlah : ", np.sum(dataset))
print("mean : ", np.mean(dataset))
print("std deviasi : ", np.std(dataset))