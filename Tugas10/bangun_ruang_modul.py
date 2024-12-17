import math
import aritmatika_modul as art

def luas_kubus(sisi):
  luas = 6 * (sisi * sisi)
  print("Luas Kubus dengan sisi ", sisi, " adalah : ", luas)

def luas_balok(l, p, t):
  luas = 2 * (l * p) + 2 * (l * t) + 2 * (t * p)
  print("Luas Balok dengan panjang ", l, "lebar", p, "tinggi", t, " adalah : ", luas)

def luas_tabung(jari_jari, tinggi):
  luas = 2 * 22/7 * jari_jari * art.tambah(jari_jari, tinggi)
  print("Luas Tabung adalah : ", luas)

def luas_bola(jari_jari):
  luas = 4 * 22/7 * jari_jari * jari_jari
  print("Luas Bola dengan jari-jari ", jari_jari, " adalah : ", luas)

def luas_kerucut(jari_jari, tinggi):
  garis_pelukis = art.pangkat(jari_jari, 2) + art.pangkat(tinggi, 2)
  luas = 22/7 * jari_jari * (jari_jari + art.akar(garis_pelukis))
  print("Luas Kerucut dengan jari-jari ", jari_jari, " dan tinggi ", tinggi, " adalah : ", luas)

def luas_limas_segitiga(sisi, tinggi):
  luas = (sisi * tinggi) / 2
  print("Luas Limas Segitiga dengan sisi ", sisi, " dan tinggi ", tinggi, " adalah : ", luas)


