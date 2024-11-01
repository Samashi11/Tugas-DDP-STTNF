# # === 1 Ganjil & Genap ====
# bilangan = int(input("Masukka Angka :"))

# if bilangan % 2 == 0:
#   print("Bilangan",bilangan,"adalah bilangan genap")
# else :
#   print("Bilangan",bilangan,"adalah bilangan ganjil")
  
# # === 2 Nilai ====
# nilai = int(input("Masukkan Nilai Ujian:"))

# print("Lulus") if nilai >= 75 else print("Tidak Lulus")

# === 3 Usia & Status ===
usia = int(input("Masukkan Usia :"))

if usia >= 18 :
  print("Dewasa")
elif usia >= 13 and usia <= 17 :
  print("Remaja")
else :
  print("Anak-Anak")
  
# === 4 Cek Keanggotaan ===
member = str(input("Masukkan Member Anda :"))

if member == "gold" or member == "silver" :
  print("Selamat! Anda mendapatkan diskon")
else :
  print("Kasian dech lo")
  
# === 5 Pembelian Diskon ===
indomie = 3500
gula = 5000
minyak = 10000

mie = int(input("Masukkan jumlah mie :"))
gul = int(input("Masukkan jumlah gul :"))
min = int(input("Masukkan jumlah min :"))

Minyak = minyak * mie
Mie = indomie * mie
Gula = gula * mie

pembelian = Mie + Gula + Minyak
diskon = pembelian * 0.9 if pembelian > 100 else pembelian

print(f"Anda Mendapatkan diskon 10%, Total setelah diskon : {diskon}") if pembelian > 100 else print(f"Tidak ada diskon, Total pembelian : {diskon}")
