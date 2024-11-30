import math

def luas_lingkaran(jari_jari):
  luas = math.pi * jari_jari * jari_jari
  print("Luas Lingkaran dengan jari-jari ", jari_jari, "adalah", luas)

def luas_persegi(sisi):
  luas = sisi * sisi
  print("Luas Persegi dengan sisi ", sisi, "adalah", luas)

def luas_persegi_panjang(panjang, lebar):
  luas = panjang * lebar
  print("Luas Persegi panjang dengan panjang ", panjang, "dan lebar", lebar, "adalah", luas)

def luas_segitiga(alas, tinggi):
  luas = 0.5 * alas * tinggi
  print("Luas Segitiga dengan alas ", alas, "dan tinggi", tinggi, "adalah", luas)

def luas_jajar_genjang(alas, tinggi):
  luas = alas * tinggi
  print("Luas Jajar Genjang dengan alas ", alas, "dan tinggi", tinggi, "adalah", luas)