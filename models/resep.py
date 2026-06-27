from typing import List
from models.bahan import Bahan

class Resep:
    def __init__(self, daftar_bahan: List[Bahan]):
        self.daftar_bahan = daftar_bahan 

    def tampilkan_resep(self) -> str:
        return ", ".join([str(b) for b in self.daftar_bahan])