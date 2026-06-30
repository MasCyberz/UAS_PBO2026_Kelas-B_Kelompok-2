from models.kue_kering import KueKering

from interfaces.pengadonan import Pengadonan
from interfaces.pengembangan import Pengembangan
from interfaces.pemanggangan import Pemanggangan
from interfaces.toping import Toping

class Muffin(
    KueKering,
    Pengadonan,
    Pengembangan,
    Pemanggangan,
    Toping
    ):
    
    def pengadonan(self):
        print("=" * 50)
        print(f"Pengadonan {self.nama}")
        print(f"{self.nama} sedang pengadonan")
        print("Pengadonan selesai.")
        
    def pengembangan(self):
        print("=" * 50)
        print(f"Pengadonan {self.nama}")
        print(f"{self.nama} sedang pengembangan")
        print("pengembangan selesai.")

    def pemanggangan(self):
        print("=" * 50)
        print(f"Pengadonan {self.nama}")
        print(f"{self.nama} sedang dipanggang.")
        print("Pemanggangan selesai.")
        
    def toping(self):
        print("=" * 50)
        print(f"Pengadonan {self.nama}")
        print(f"{self.nama} sedang diberi topping.")
        print("Pemberian toping selesai.")