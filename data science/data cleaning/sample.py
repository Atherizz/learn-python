# # menghapus yang kosong
# df.dropna()
# df = df.dropna(axis=1)

# # mengisi yg kosong jadi 0
# df["column_name"] = df["column_name"].fillna()

# df.fillna(method="ffill")
# df.fillna(method="bfill")


# df["column_name"] = df["column_name".interpolate()]

# #rename
# df = df.rename(columns={"old name" : "new name"})

# # ganti tipe data
# df["column_name"] = df["column_name"].astype("float")
# df["column_name"] = pd.to_datetime(df["column_name"])

# #modifikasi
# df["new_column"] = df["existing_column"] * 2

# # combining & merge
# combined = pd.concat([df1,df2], axis=0)
# combined = pd.concat([df1,df2], axis=1)

# merged = pd.merge(df1, df2, on="common_column")
# merged = pd.merge(df1, df2, how="left" on="common_column")
# merged = pd.merge(df1, df2, how="inner" on="common_column")

# joined = df1.join(df2, how="inner")