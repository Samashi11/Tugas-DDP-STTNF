class Gempa:
  def __init__(self, lokasi, skala):
    self.skala = skala
    self.lokasi = lokasi

  def dampak(self):
    if self.skala < 2:
      print("Dampak Gempa di", self.lokasi, "dengan skala", self.skala, "Tidak Berasa")
    elif self.skala >= 2 and self.skala <= 4:
      print("Dampak Gempa di", self.lokasi, "dengan skala", self.skala, "Bangunan Retak-Retak")
    elif self.skala > 4 and self.skala <= 6:
      print("Dampak Gempa di", self.lokasi, "dengan skala", self.skala, "Bangunan Roboh")
    elif self.skala > 6:
      print("Dampak Gempa di", self.lokasi, "dengan skala", self.skala, "Bangunan Roboh dan Berpotensi Tsunami")