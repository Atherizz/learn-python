import pandas as pd

# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

print("First 10 rows : \n" , df.head(10))
print("Last 5 rows : \n" , df.tail(5))
print("Info : \n", df.info())
print("Describe : \n", df.describe())

selected_columns = df[["species", "sepal_length"]]
print("Selected Columns : \n", selected_columns)

filter_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "virginica")]
print("filter rows : \n", filter_rows)

