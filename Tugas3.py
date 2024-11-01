print("1 === Biodata Diri ===")
nama = "Salman Maula Ash-Shidqi"
nim = "0110224157"
rombel = "TI0"
no_telp = "081318288133"
alamat = """Jalan Samudra Jaya, Kp Grogol, RT 03/02 No 7A"""

print("Nama          :",nama)
print("NIM           :",nim)
print("Rombel        :",rombel)
print("Nomor Telepon :",no_telp)
print("Alamat        :",alamat)

print("\n ")
print("2 === Biodata Teman ===")
nama_teman = "Wahyu Ahmad Yassin"
nim_teman = "0110224047"
rombel_teman = "TI0"
no_telp_teman = 62895604849987
alamat_teman = """Jl. Letnan Murod Lrg.Cempedak No.717
Palembang
"""

print("Nama          :",nama_teman)
print("NIM           :",nim_teman)
print("Rombel        :",rombel_teman)
print("Nomor Telepon :",no_telp_teman)
print("Alamat        :",alamat_teman)

print("\n ")
print("3 === Menghitung Berat Badan Ideal ===")
#input
tinggi = int(input("masukkan tinggi badan (cm) : "))

#proses
bbi = float((tinggi - 100) * 0.9)

#output
print("berat badan ideal dari tinggi",tinggi,"cm \nadalah",bbi,"kg")

print("\n ")
print("4 === Mengubah Celcius ke Fahrenheit ===")
#input
celcius = int(input("Masukkan nilai Celcius :"))

#proses
fahrenheit = int((celcius * 9/5) + 32)

#output
print("Konversi dari", celcius, "°C sama dengan",fahrenheit,"°F")

print("\n ")
print("5 === Hitung Luas & Keliling Tabung ===")
#input
tinggi = int(input("Masukkan Tinggi (cm):"))
jari = int(input("Masukkan Jari² (cm):"))

#proses
luas = 2 * 22/7 * jari * (jari + tinggi)
keliling = 2 * 22/7 * jari

#output
print("Luas Tabung dengan tinggi",tinggi,"cm dan dengan jari²",jari,"cm \nadalah",int(luas),"cm²\n\nKeliling Tabungnya adalah",int(keliling),"cm")