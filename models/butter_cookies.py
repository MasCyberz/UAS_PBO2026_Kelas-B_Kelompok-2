from models.kue_kering import KueKering
from interfaces.pengadonan import Pengadonan
from interfaces.pemanggangan import Pemanggangan
from interfaces.toping import Toping

class ButterCookies(KueKering,
    Pengadonan,
    Pemanggangan,
    Toping):
    def pengadonan(self):
        print(f"{self.nama} sedang pengadonan")
        
    def pemanggangan(self):
        print(f"{self.nama} sedang dipanggang.")
        
    def toping(self):
        print(f"{self.nama} diberi topping.")