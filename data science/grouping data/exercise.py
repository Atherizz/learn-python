import pandas as pd

data = {
    "Class": ["A", "B", "C", "B", "B", "A", "C", "A", "B", "C"],
    "Score": [85, 78, 92, 74, 88, 90, 95, 80, 76, 89],
    "Age": [15, 16, 17, 16, 15, 17, 18, 16, 15, 17]
}

df = pd.DataFrame(data)

# print("Original Dataset: \n", df)

grouped = df.groupby("Class").mean()
# print(grouped)

stats = df.groupby("Class").agg(
    {"Score":["mean","max","min"], "Age":["mean","max","min"]},
    )
print(stats)

score_mean = df["Score"].mean()
print(score_mean)

selected_column = df["Score", "Age"]
print(selected_column)