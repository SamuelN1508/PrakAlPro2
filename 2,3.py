# Masukan Gaji Perjam dan Jam Kerja
gaji_perjam = int(input("Masukan gaji perjam : "))
jam_minggu = int(input("Masukan jam per minggu :"))

# Menghitung Gaji Kotor 
kotor = gaji_perjam * (5*jam_minggu)

# Menghitung Gaji Bersih Dengan Pajak
bersih = kotor - (kotor * 0.14)

# Menghitung Uang Sisa Setelah Pembelian Pakaian
pembelian_pakaian = bersih - (bersih * 0.10)

# Menghitung Uang Sisa Setelah Pembelian Alat Tulis
pembelian_alattulis = pembelian_pakaian - (bersih * 0.1)

# Menghitung Uang Yang Akan Disedekahkan
sedekah = pembelian_alattulis - (pembelian_alattulis*0.25)

# Menghitung Uang Sedekah Untuk Anak Yatim
yatim = ((sedekah * 0.30) // 1000) * 100

# Menghitung Uang Sedekah Untuk Anak Dhuafa
dhuafa = sedekah - yatim

# Print Semua Jawaban
print("Pendapatan Budi Sebelum Pajak : " , kotor)
print("Pendapatan Budi Setelah Pajak :" , bersih)
print("Jumlah Uang Habis untuk pembelian pakaian : ", pembelian_pakaian)
print("Jumlah Uang Habis untuk pembelian alat tulis : ", pembelian_alattulis)
print("Jumlah Uang Habis untuk sedekah : ", sedekah)
print("Jumlah Uang Diterima Yatim : ", yatim)
print("Jumlah Uang Diterima Dhuafa : ", dhuafa)