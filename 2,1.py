# Input Untuk Memasukan Tinggi Badan
tinggi = float(input("Masukan tinggi badan anda (m): ")) 

# Info BMI
print("UNDERWEIGHT <18.5\nNORMAL 18.5-24.9\nOVERWEIGTH 25-29.9\nOBESE 30-34.9\nEXTREMELY OBESE 35>") 

# Masukan BMI
BMI = float(input("Masukan Body Mass Index yang diinginkan : ")) 

# Rumus Menghitung BMI Adalah Berat/Tinggi**2 Diubah Menjadi Berat = BMI*Tinggi**2
berat = BMI * tinggi**2 

# Mencetak Hasil
print(f"Untuk mencapai Body Mass Index yang anda inginkan, berat badan harus mencapai {berat} Kg") 