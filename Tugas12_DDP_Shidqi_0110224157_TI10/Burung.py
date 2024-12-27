from Animal import *

class Burung(Animal) :
  def __init__(self, name, makanan, hidup, berkembangbiak, paruh, warna) :
    super().__init__(name, makanan, hidup, berkembangbiak)
    self.paruh = paruh
    self.warna = warna

  def info_burung(self) :
    super().info_animal()
    print(
    "Paruh\t\t:", self.paruh, 
    "\nWarna\t\t:", self.warna,
    "\n------------------------------"
    )

kecapi = Burung("Kecapi", "Biji-Bijian", "Langit Ke-7", "Bertelur", "Bengkok", "Hitam")
print("\tIngfo Buwung")
kecapi.info_burung()

merak = Burung("Merak", "Serealia", "Darat", "Bertelur", "Panjang", "Merah")
merak.info_burung()

kakatua = Burung("Kakatua", "Biji-Bijian", "Darat", "Bertelur", "Bengkok", "Putih")
kakatua.info_burung()
