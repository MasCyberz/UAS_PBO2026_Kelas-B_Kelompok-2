class ProductionView:
    @staticmethod
    def jalankan_simulasi(daftar_produk, service):
        print("\n--- SIMULASI PRODUKSI ---")
        if not daftar_produk:
            print("Belum ada produk di sistem.")
            return

        for i, p in enumerate(daftar_produk):
            print(f"{i+1}. {p.nama}")
            
        try:
            idx = int(input("\nPilih nomor roti untuk disimulasikan: ")) - 1
            if 0 <= idx < len(daftar_produk):
                print(f"\n--- Memulai Alur Produksi: {daftar_produk[idx].nama} ---")
                # Memanggil logika simulasi dari bakery_service (Tugas Dimas)
                service.simulasi_produksi(daftar_produk[idx])
            else:
                print("Nomor roti tidak valid.")
        except ValueError:
            print("Input harus berupa angka!")
