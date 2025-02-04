import pandas as pd
# Load Dataset
data = pd.read_csv("sales-data-sample.csv")

df = data.head(50)
print(df)

# grouped = df.groupby("City").agg({
#     "latitude" : ["mean", "max", "min"], "longitude" : ["mean", "max", "min"]
# })
# print(grouped)

# pivot = df.pivot_table(
#     values="lat",
#     index="category_column",
#      aggfunc="mean"
# )

# print("First 10 rows : \n" , df.head(10))