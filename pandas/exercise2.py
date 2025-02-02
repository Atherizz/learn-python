import pandas as pd

# df = pd.read_excel("ekskul .xlsx")

# print("First 10 rows : \n" , df.head())

data = {
    "Nama": ["Andi", "Budi", "Cici", "Dedi", "Eva"],
    "Usia": [21, 22, 20, 23, 24],
    "Kota": ["Jakarta", "Bandung", "Surabaya", "Medan", "Yogyakarta"],
    "Pekerjaan": ["Data Scientist", "Software Engineer", "UI/UX Designer", "Product Manager", "Data Analyst"],
    "Gaji": [8000000, 9500000, 7500000, 12000000, 8500000]
}

df = pd.DataFrame(data)
print(df)

df["Bonus"] = [500000, 600000, 400000, 700000, 550000]
print(df)

print("Mean Gaji : ", df["Gaji"].mean() )

selected_column = df[["Nama", "Pekerjaan"]]
print(selected_column)

selected_column.to_csv("data.csv", index=False)