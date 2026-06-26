class TambahProductView:
    @staticmethod
    def tambah_produk():
        print("\n--- TAMBAH PRODUK BARU ---")
        try:
            nama = input("Masukkan Nama Produk: ")
            kode = input("Masukkan Kode Produk: ")
            
            bahan_input = input("Masukkan Bahan Baku (pisahkan dengan koma): ")
            bahan_baku = [bahan.strip() for bahan in bahan_input.split(',')]
            
            biaya = float(input("Masukkan Total Biaya Produksi (Rp): "))
            harga = float(input("Masukkan Total Harga Jual (Rp): "))
            pcs = int(input("Masukkan Jumlah pcs per Resep: "))
            
            print(f"\nBerhasil merekam draf produk {nama}. (Harap sinkronkan ke Service)")
            # Mengembalikan data sebagai dictionary atau tuple agar diproses oleh Service
            return nama, kode, bahan_baku, biaya, harga, pcs
            
        except ValueError:
            print("Gagal menambahkan produk. Pastikan harga dan pcs diisi angka!")
            return None
