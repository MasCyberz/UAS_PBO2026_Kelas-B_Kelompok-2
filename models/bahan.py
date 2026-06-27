class Bahan:
    def __init__(self, nama: str, jumlah: float, satuan: str):
        self.nama = nama
        self.jumlah = jumlah
        self.satuan = satuan

    def __str__(self):
        return f"{self.nama} ({self.jumlah} {self.satuan})"