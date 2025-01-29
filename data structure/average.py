# grade = {"savero" : 96, "budi" : 67, "ray" : 78, "rahma" : 94, "eko" : 65}
nilai = {}
jumlah = int(input("masukkan jumlah siswa : "))
total = 0

for i in range (jumlah):
    name = input("masukkan nama : ")
    grade = int(input("masukkan nilai : "))
    nilai[name] = grade
    total += grade
    avg = total / jumlah

print(nilai, avg)

