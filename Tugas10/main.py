import bangun_datar_modul as bdm
import bangun_ruang_modul as brm

print("\n Pilih Operasi yang dilakukan :")
print("1.Luas Bangun Datar")
print("2.Luas Bangun Ruang")
pilih1 = int(input("Masukkan pilihan operasi : "))

if pilih1 == 1:
  print("\n Pilih Bangun Datar yang diinginkan :")
  print("1.Persegi")
  print("2.Persegi Panjang")
  print("3.Segitiga")
  print("4.Lingkaran")
  print("5.Jajar Genjang")
  pilih2 = int(input("Masukkan pilihan bangun datar : "))
  if pilih2 == 1:
    sisi = int(input("Masukkan panjang sisi : "))
    bdm.luas_persegi(sisi)
  elif pilih2 == 2:
    panjang = int(input("Masukkan panjang : "))
    lebar = int(input("Masukkan lebar : "))
    bdm.luas_persegi_panjang(panjang, lebar)
  elif pilih2 == 3:
    alas = int(input("Masukkan alas : "))
    tinggi = int(input("Masukkan tinggi : "))
    bdm.luas_segitiga(alas, tinggi)
  elif pilih2 == 4:
    jari_jari = int(input("Masukkan jari-jari : "))
    bdm.luas_lingkaran(jari_jari)
  elif pilih2 == 5:
    alas = int(input("Masukkan alas : "))
    tinggi = int(input("Masukkan tinggi : "))
    bdm.luas_jajar_genjang(alas, tinggi)
  else:
    print("Pilihan tidak tersedia")
elif pilih1 == 2:
  print("\n Pilih Bangun Ruang yang diinginkan :")
  print("1.Kubus")
  print("2.Balok")
  print("3.Tabung")
  print("4.Bola")
  print("5.Kerucut")
  pilih3 = int(input("Masukkan pilihan bangun ruang : "))
  if pilih3 == 1:
    sisi = int(input("Masukkan sisi : "))
    brm.luas_kubus(sisi)
  elif pilih3 == 2:
    panjang = int(input("Masukkan panjang : "))
    lebar = int(input("Masukkan lebar : "))
    tinggi = int(input("Masukkan tinggi : "))
    brm.luas_balok(panjang, lebar, tinggi)
  elif pilih3 == 3:
    jari = int(input("Masukkan jari-jari : "))
    tinggi = int(input("Masukkan tinggi : "))
    brm.luas_tabung(jari, tinggi)
  elif pilih3 == 4:
    jari = int(input("Masukkan jari-jari : "))
    brm.luas_bola(jari)
  elif pilih3 == 5:
    jari = int(input("Masukkan jari-jari : "))
    tinggi = int(input("Masukkan tinggi : "))
    brm.luas_kerucut(jari, tinggi)
  else:
    print("Pilihan tidak tersedia")
else:
  print("Pilihan tidak tersedia")