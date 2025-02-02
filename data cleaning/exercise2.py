import pandas as pd

# Dataset Siswa
data_siswa = {
    "nis": [101, 102, 103, 104, 105, 106],
    "nama": ["Alex", "Bella", "Charlie", "Diana", "Erik", "Fiona"],
    "kelas": ["A", "A", "B", "B", "C", "C"]
}
df_siswa = pd.DataFrame(data_siswa)

# Dataset Nilai Matematika
data_mat = {
    "nis": [101, 102, 111, 123, 107],
    "nilai_matematika": [85, 90, 78, 88, 95]
}
df_mat = pd.DataFrame(data_mat)

# Dataset Nilai Bahasa Inggris
data_inggris = {
    "nis": [102, 103, 104, 106, 108],
    "nilai_inggris": [88, 85, 92, 78, 89]
}
df_inggris = pd.DataFrame(data_inggris)

#INNER JOIN
merged_inner = pd.merge(df_siswa, df_mat, how="inner",on="nis")
print("Gabungan Keseluruhan : \n", merged_inner)
print()

#LEFT JOIN
merged_left = pd.merge(df_siswa, df_mat, how="left",on="nis")
nilai_kosong = merged_left["nilai_matematika"].isna().sum()
print("Jumlah nilai mat yg kosong: ", nilai_kosong)
print("Left Join : \n", merged_left)
print()

#RIGHT JOIN
merged_right = pd.merge(df_siswa, df_mat, how="right",on="nis")
nilai_tanpa_id = merged_right["nama"].isna().sum()
print("Jumlah nilai tanpa NIS: ", nilai_tanpa_id)
print("Left Join : \n", merged_right)

#MULTIPLE MERGE
gabungan_data = df_siswa.merge(df_mat, on="nis", how="left")\
                         .merge(df_inggris, on="nis", how="left")
nilai_lengkap = gabungan_data.dropna().shape[0]
print("\nSolusi 3:")
print("Jumlah siswa dengan nilai lengkap:", nilai_lengkap)
print(gabungan_data)
print()

jumlah_nan = gabungan_data.isna().sum()

# DROP COLUMNS 
for i in range(len(jumlah_nan)):
    # persentase_nan = jumlah_nan.iloc[i] / len(gabungan_data)
    # if persentase_nan > 0.5:
    if jumlah_nan.iloc[i] > 0.5 * len(gabungan_data):
        gabungan_data.drop(gabungan_data.columns[i], axis=1, inplace=True)
        
print("Data yang telah dihapus : \n", gabungan_data)

one_hot = pd.get_dummies(gabungan_data, columns=['nilai_inggris'])
print("Hasil menggunakan pd.get_dummies():\n", one_hot)




