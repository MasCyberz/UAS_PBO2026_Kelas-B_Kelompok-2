class BakeryProduct:
    def __init__(self, nama, jumlah_produksi):
        self.nama = nama
        self.jumlah_produksi = jumlah_produksi
        self.resep = {}

    def tampilkan_info(self):
        print(f"\n=== {self.nama} ===")
        print(f"Jumlah Produksi : {self.jumlah_produksi}")
        print("\nBahan Baku : ")
        for bahan, jumlah in self.resep.items():
            print(f"- {bahan} : {jumlah}")