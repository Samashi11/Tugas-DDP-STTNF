print()
print("## Nomor 1 ##")

def celcius_ke_fahrenheit(celcius):
  konversi = (celcius * 9/5) + 32
  return konversi

print(celcius_ke_fahrenheit(0))

print()
print("## Nomor 2 ##")

def is_genap(bilangan):
  penentu = bilangan % 2 == 0
  return penentu

print(is_genap(2))
print(is_genap(3))

print()
print("## Nomor 3 ##")

def Lulus_LidakLulus(nilai):
  penentu = nilai
  if nilai >= 80:
    penentu = "Lulus"
  elif nilai <= 60:
    penentu = "TIdak Lulus"
  else:
    penentu = "Tidak Valid"
  return penentu

print(Lulus_LidakLulus(60))

print()
print("## Nomor 4 ##")

def Ganjil_Dibawah_Argumen(angka):
  for i in range(angka):
    if i % 2 != 0:
      print(i)

print(Ganjil_Dibawah_Argumen(20))