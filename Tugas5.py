# 1 === List Kendaraan ===
kendaraan = ['beat mber', 'motor', 200, 'pink', 2]
kendaraan.append('13jt')
kendaraan.append('matic')
kendaraan.insert(2,'honda')

print(kendaraan)
print(type(kendaraan))
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))
print(type(kendaraan[7]))

# 2 === Match Case ===
print("""
1. Hitung Luas Persegi
2. Hitung Luas Lingkaran
3. Hitung Luas Segitiga
""")
hitung_luas = input('Pilih Antara Angka 1 - 3 :')

match hitung_luas:
  case '1':
    print("Menghitung Luas Persegi")
    sisi = int(input("Masukkan Sisi :"))
    luas_persegi = sisi * sisi
    print(f'luas persegi dari sisi {sisi} cm adalah {luas_persegi} cm^2')
  case '2':
    print("Menghitung Luas Lingkaran")
    jari = int(input("Masukkan Jari-Jari :"))
    luas_lingkaran = 3.14 * jari**2
    print(f'Luas Lingkaran dari jari² {jari} cm adalah {luas_lingkaran} cm')
  case '3':
    print("Menghitung Luas Segitiga")
    a = int(input("Masukkan Alas :"))
    t = int(input("Masukkan Tinggi :"))
    luas_segitiga = 1/2 * a *t
    print(f'Luas Segitiga dari alas {a} cm dan tinggi {t} cm adalah {luas_segitiga} cm')
  case _:
    print("Angka Tidak Valid")

