import numpy as np

skor_ujian = np.array([78, 85, 90, 65, 88, 92, 76, 81, 70, 95])

x_min = np.min(skor_ujian)
x_max = np.max(skor_ujian)

normalized_array = (skor_ujian - x_min) / (x_max - x_min)
print(normalized_array)