class Bahan:
    def __init__(self, kode: str, nama: str, satuan: str, stok: float, harga: float):
        self.kode = kode
        self.nama = nama
        self.satuan = satuan
        self.stok = stok
        self.harga = harga

    def __str__(self):
        return self.nama