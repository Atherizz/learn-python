import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Menampilkan pola atau hubungan antar variabel dalam jumlah besar
# Melihat korelasi antar data
# Menganalisis distribusi data dalam bentuk matriks
data = np.random.rand(5,5)
print(data)
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("HeatMap")
# sns.pairplot(df)
plt.show()