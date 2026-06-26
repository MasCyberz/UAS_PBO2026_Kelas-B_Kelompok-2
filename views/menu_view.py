class MenuView:
    @staticmethod
    def tampilkan_menu():
        print("\n=== SISTEM MANAJEMEN HANARI BAKERY ===")
        print("1. Tambah Produk Baru")
        print("2. Tampilkan Semua Produk")
        print("3. Kalkulator Profit")
        print("4. Simulasi Proses Produksi")
        print("5. Keluar")
        return input("Pilih menu (1-5): ")

    @staticmethod
    def tampilkan_pesan(pesan):
        print(f"\n{pesan}")
