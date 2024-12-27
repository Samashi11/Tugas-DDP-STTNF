from Animal import *

class Ikan(Animal) :
  def __init__(self, name, makanan, hidup, berkembangbiak, bernavas, air) :
    super().__init__(name, makanan, hidup, berkembangbiak)
    self.bernavas = bernavas
    self.air = air

  def info_ikan(self) :
    super().info_animal()
    print(
    "Navas dengan\t:", self.bernavas, 
    "\nJenis Air\t:", self.air,
    "\n-------------------------------"
    )

paus = Ikan("Paus", "Plankton", "Laut", "Melahirkan", "Insang", "Asin")
print("\tIngfo Ikang")
paus.info_ikan()

lumba_lumba = Ikan("Lumba-lumba", "Ikan Kecil", "Laut", "Melahirkan", "Insang", "Asin")
lumba_lumba.info_ikan()

lele = Ikan("Lele", "Cacing", "Sungai", "Bertelur", "Insang", "Tawar")
lele.info_ikan()
