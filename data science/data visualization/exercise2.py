import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("sales-data-sample.csv")

penjualan = pd.DataFrame(data)

df = data.head(20)[["Country", "Sales"]]

plt.bar(df["Country"],df["Sales"], color="green")
plt.title("Country Sales Data")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.show()    






# # Calculate correlation matrix
# del df['species']
# correlation_matrix = df.corr()

# #plot heatmap
# sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()