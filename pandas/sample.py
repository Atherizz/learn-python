import pandas as pd

s = pd.Series([10,20,30], index=["a", "b", "c"])
#  

data = {"Name" : ["Agus", "Roni"], "Age" : [21, 32]}
df = pd.DataFrame(data)
# print(df)

#Viewing Data
print("Head : \n", df.head())
print("Tail: \n", df.tail(3))

print("Info : \n", df.info())
print("Describe : \n", df.describe())

# selected columns
print(df[["Name", "Age"]])

# selecting by condition
print(df[df["Age"] > 25 ])

# selecting by position
print(df.iloc[:, 0])

# selecting by label
print(df.loc[0])
print(df.loc[:, ["Name"]])


# df = pd.read_csv("data.csv")
# df.to_csv("data.csv", index=False)
# df = pd.read_excel("nilaisem.xlsx", index=False)