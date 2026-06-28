from models.bahan import Bahan

class DetailResep:
    def __init__(
        self,
        bahan: Bahan,
        jumlah: float
    ):
        self.bahan = bahan
        self.jumlah = jumlah
        