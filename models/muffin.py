from models.kue_kering import KueKering

from interfaces.pengadonan import Pengadonan
from interfaces.pengembangan import Pengembangan
from interfaces.pemanggangan import Pemanggangan

class Muffin(
    KueKering,
    Pengadonan,
    Pengembangan,
    Pemanggangan
    ):
    
    def pengadonan(self):
        print(f"{self.nama} sedang pengadonan")
        
    def pengembangan(self):
        print(f"{self.nama} sedang melalui proses pengembangan.")

    def pemanggangan(self):
        print(f"{self.nama} sedang dipanggang.")