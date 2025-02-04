import matplotlib.pyplot as plt

#line plot
# Digunakan untuk menunjukkan tren atau perubahan data dari waktu ke waktu.
# Cocok untuk data berurutan seperti pertumbuhan penjualan tahunan, suhu harian, atau jumlah pengguna dari tahun ke tahun.
# Setiap titik dihubungkan dengan garis untuk memperjelas pola atau kecenderungan dalam data.
years = [2021,2022,2023,2024]
sales = [100,200,300, 500]
plt.plot(years, sales, label="Sales Trend", color="blue", marker="o")
plt.title("Sales over Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend()
plt.show()

# Bar chart
# Digunakan untuk membandingkan kategori data secara langsung.
# Setiap kategori memiliki satu batang dengan panjang sesuai nilai datanya.
# Tidak harus data berurutan (misalnya kategori produk, wilayah, atau departemen dalam perusahaan).
categories = ["Electronics", "Clothing", "Beauty", "Food", "Accessories"]
revenues = [250,400,125,300,350]
plt.bar(categories,revenues, color="green")
plt.title("Revenue by Categories")
plt.show()

# Scatter Plot
# Menunjukkan hubungan atau korelasi antara dua variabel.
# Setiap titik mewakili satu pasangan data (x, y).
# Digunakan untuk melihat pola, outlier, atau kekuatan hubungan antara variabel.
hours_studied = [1,2,3,4,5]
exam_score = [65,70,80,85,90]
plt.scatter(hours_studied, exam_score, color="red")
plt.title("Exam Score based on hours studies")
plt.show()