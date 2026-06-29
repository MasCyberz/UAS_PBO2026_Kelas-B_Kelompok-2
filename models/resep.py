from models.detail_resep import DetailResep

class Resep:
    def __init__(self, kode:str, nama:str, daftar_bahan:None):
        self.kode = kode
        self.nama = nama
        self.daftar_bahan = daftar_bahan or []