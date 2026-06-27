class ProductView:
    @staticmethod
    def tampilkan_semua(daftar_produk):
        print("\n--- DAFTAR PRODUK ---")
        if not daftar_produk:
            print("Belum ada produk yang terdaftar.")
            return

        for p in daftar_produk:
            print(f"[{p.kode}] {p.nama} (Resep dasar untuk {p.pcs_per_resep} pcs)")
            bahan_digabung = ", ".join(p.bahan_baku)
            print(f"Bahan baku     : {bahan_digabung}")
            print(f"Biaya Produksi : Rp{p.biaya_produksi:,.0f}")
            print(f"Harga Jual     : Rp{p.harga_jual:,.0f}")
            print("-" * 40)
