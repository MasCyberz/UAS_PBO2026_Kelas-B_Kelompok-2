class ProfitView:
    @staticmethod
    def jalankan_kalkulator(daftar_produk):
        print("\n--- KALKULATOR PROFIT ---")
        if not daftar_produk:
            print("Belum ada produk di sistem.")
            return

        for i, p in enumerate(daftar_produk):
            print(f"{i+1}. {p.nama}")
        
        try:
            idx = int(input("\nPilih nomor roti: ")) - 1
            if 0 <= idx < len(daftar_produk):
                target = int(input("Masukkan target produksi (pcs): "))
                produk_terpilih = daftar_produk[idx]
                
                # Menghitung profit dari model
                profit, biaya, dapat = produk_terpilih.hitung_profit(target)
                bahan_digabung = ", ".join(produk_terpilih.bahan_baku)
                
                # Output sesuai format laporan
                print(f"\nNama Projek  : {produk_terpilih.nama}")
                print(f"Bahan baku   : {bahan_digabung}")
                print(f"Jumlah pcs   : {target} pcs")
                print(f"Pengeluaran  : Rp{biaya:,.0f}")
                print(f"Pendapatan   : Rp{dapat:,.0f}")
                print(f"Profit       : Rp{profit:,.0f}")
            else:
                print("Nomor roti tidak valid.")
        except ValueError:
            print("Input harus berupa angka!")
