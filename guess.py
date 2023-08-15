import random

class angka:
  def __init__(self):
    self.tebakan = 0
    self.jawaban = random.randint(1,10)

  def cek(self):
    if self.tebakan == self.jawaban:
     return True
     return False