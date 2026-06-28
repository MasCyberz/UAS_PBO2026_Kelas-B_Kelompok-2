from models.bakery_product import BakeryProduct

from interfaces.pengadonan import Pengadonan
from interfaces.pengembangan import Pengembangan
from interfaces.pemanggangan import Pemanggangan

class Croissant(
    BakeryProduct,
    Pengadonan,
    Pengembangan,
    Pemanggangan
):
    def pengadonan(self):
        print("=" * 50)
        print(f"Pengadonan {self.nama}")
        print("Mencampur seluruh bahan...")
        print("Pengadonan selesai.")
        
    def pengembangan(self):
        print("=" * 50)
        print(f"Pengembangan {self.nama}")
        print("Melakukan pengembangan...")
        print("Pengembangan selesai.")
    
    def pemanggangan(self):
        print("=" * 50)
        print(f"Pemanggangan {self.nama}")
        print("Melakukan pemanggangan...")
        print("Pemanggangan selesai.")