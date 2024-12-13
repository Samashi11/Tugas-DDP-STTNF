from Animal import *

class Ular(Animal) :
  def __init__(self, name, makanan, hidup, berkembangbiak, bisa, habitat) :
    super().__init__(name, makanan, hidup, berkembangbiak)
    self.bisa = bisa
    self.habitat = habitat

  def info_ular(self) :
    super().info_animal()
    print(
    "Bisa\t\t:", self.bisa, 
    "\nHabitat\t\t:", self.habitat,
    "\n------------------------------"
    )

sanca = Ular("Sanca", "Sapi", "Darat", "Bertelur Melahirkan", "Mematikan", "Rawa")
print("\tIngfo Oray")
sanca.info_ular()

king_cobra = Ular("King Cobra", "Tikus", "Darat", "Bertelur", "Mematikan", "Hutan")
king_cobra.info_ular()

python = Ular("Python", "Kambing", "Darat", "Bertelur", "Tidak Berbisa", "Hutan")
python.info_ular()
