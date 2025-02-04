import pandas as pd
import numpy as np

data = {
    "name": ["Andi", "Budi",np.nan, "Dedi", "Eka"],
    "age": [21, np.nan, 20, 23, 19],
    "score": [85, 90, 78, np.nan, 92]
}

df = pd.DataFrame(data)
print("Original Dataset: \n", df)
print()

df["name"] = df["name"].fillna("Unnamed")
df["age"] = df["age"].fillna(df["age"].mean())
df["score"] = df["score"].fillna(0)

df = df.rename(columns={"score" : "point"})

print("New Dataset: \n", df)

data1 = {
    "id": [1, 2, 3, 4, 5],
    "name": ['Andi', 'Budi', 'Cici', 'Dedi', 'Eka'],
    "age": [21, 22, 20, 23, 19]
}
df1 = pd.DataFrame(data1)

data2 = {
    'id': [1, 2, 3, 4, 5],
    'score': [96, 87, 78,75, 90]
}
df2 = pd.DataFrame(data2)

merged = pd.merge(df1, df2, how="left", on="id")
print("merged Dataset: \n", merged)

merged["score_percentage"] = (merged["score"] / 100) * 100
print("Transformed Dataset: \n", merged)
