import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
 #Load Dataset
 
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

#Inspect Data
print(df.info())
print(df.describe())
 
 # Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove duplicate
df = df.drop_duplicates()

# Filter Data Passengers in first class
first_class = df[df["Pclass"] == 1]
print("First class Passengers: \n", first_class.head())

# Bar Chart: Survival rate by Class
# survival_by_class = df[["Pclass"], ["Survived"]]
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival Rate by Class")
plt.ylabel("Survival Rate")
plt.show()

# Histogram: Age Distribution
# data = df["Age"]
# plt.hist(data, bins=4, color="green", edgecolor="black")
# plt.title("Age Distribution")
# plt.show()
sns.histplot(df["Age"], kde=True, bins=20, color="green")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="green")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
