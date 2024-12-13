# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
# buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method  
# buat minimal 3 objek dari masing masing class child

class Animal :
  def __init__(self, name, makanan, hidup, berkembangbiak) :
    self.name = name
    self.makanan = makanan
    self.hidup = hidup
    self.berkembangbiak = berkembangbiak

  def info_animal(self) :
    print(
    "Nama Hewan\t:", self.name,
    "\nMakanan\t\t:", self.makanan,
    "\nHidup\t\t:", self.hidup,
    "\nBerkembang Biak\t:", self.berkembangbiak
    )

# kucing = Animal("Kucing", "Daging", "Darat", "Melahirkan")
# kucing.info_animal()