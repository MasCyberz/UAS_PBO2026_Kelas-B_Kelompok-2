from abc import ABC

class BakeryProduct(ABC):
    def __init__(self, kode: str, nama: str, harga_jual: float, batch_size: int, resep):
        self.kode = kode
        self.nama = nama
        self.harga_jual = harga_jual
        self.batch_size = batch_size
        self.resep = resep

    def __str__(self):
        return (
            f"[{self.kode}] "
            f"{self.nama}"
        )