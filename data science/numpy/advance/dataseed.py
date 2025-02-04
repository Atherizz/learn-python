import numpy as np

np.random.seed(115312)

random_array = np.random.rand(3,3)
print("Random array : \n", random_array)
print()

random_int = np.random.randint(0,10, size=(2,3))
print("Random Integer : \n", random_int)