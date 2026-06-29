from views.input_view import InputView


class ProductionView:

    @staticmethod
    def menu(bakery):

        while True:
            print("\n=== MENU PRODUKSI ===")
            print("1. Jalankan Produksi")
            print("2. Simulasi Proses Produksi")
            print("3. Riwayat Produksi")
            print("0. Kembali")

            pilihan = input("Pilih: ")

            if pilihan == "1":
                ProductionView.jalankan_produksi(bakery)

            elif pilihan == "2":
                ProductionView.jalankan_simulasi(bakery)

            elif pilihan == "3":
                riwayat = bakery.production_service.get_riwayat()
                ProductionView.tampilkan_riwayat(riwayat)
                total_produk = bakery.production_service.total_produksi()
                total_biaya = bakery.production_service.total_biaya_produksi()
                ProductionView.tampilkan_ringkasan(total_produk, total_biaya)

            elif pilihan == "0":
                break

            else:
                print("Menu tidak valid.")

    @staticmethod
    def jalankan_produksi(bakery):
        try:
            kode, batch = ProductionView.input_produksi()
            hasil = bakery.production_service.produksi(kode, batch)
            ProductionView.tampilkan_hasil(hasil)
        except Exception as e:
            ProductionView.tampilkan_error(e)

    @staticmethod
    def jalankan_simulasi(bakery):
        try:
            print("\n=== SIMULASI PROSES PRODUKSI ===")
            daftar = bakery.produk_service.get_all_produk()

            if not daftar:
                print("Belum ada produk.")
                return

            for i, p in enumerate(daftar, 1):
                print(f"{i}. [{p.kode}] {p.nama}")

            pilihan = InputView.input_int("Pilih nomor produk")
            if pilihan < 1 or pilihan > len(daftar):
                print("Nomor tidak valid.")
                return

            produk = daftar[pilihan - 1]
            print(f"\n--- Memulai Simulasi: {produk.nama} ---")
            bakery.production_service.jalankan_proses(produk)
            print("--- Simulasi Selesai ---")

        except Exception as e:
            ProductionView.tampilkan_error(e)

    @staticmethod
    def input_produksi():
        print("\n")
        print("=" * 50)
        print("JALANKAN PRODUKSI")
        print("=" * 50)
        return (
            InputView.input_string("Kode Produk"),
            InputView.input_int("Jumlah Batch")
        )

    @staticmethod
    def tampilkan_hasil(hasil):
        print("\n")
        print("=" * 60)
        print("HASIL PRODUKSI")
        print("=" * 60)
        print(f"Kode Produk      : {hasil['kode_produk']}")
        print(f"Nama Produk      : {hasil['nama_produk']}")
        print(f"Jumlah Batch     : {hasil['jumlah_batch']}")
        print(f"Jumlah Produk    : {hasil['jumlah_produk']} pcs")
        print(f"Biaya Produksi   : Rp {hasil['biaya_produksi']:,.0f}")
        print(f"Status           : {hasil['status']}")
        print("=" * 60)

    @staticmethod
    def tampilkan_riwayat(riwayat):
        print("\n")
        print("=" * 90)
        print("RIWAYAT PRODUKSI")
        print("=" * 90)

        if not riwayat:
            print("Belum ada riwayat produksi.")
            return

        print(
            f"{'Kode':<10}"
            f"{'Nama Produk':<25}"
            f"{'Batch':>10}"
            f"{'Jumlah':>12}"
            f"{'Biaya':>18}"
        )
        print("-" * 90)

        for item in riwayat:
            print(
                f"{item['kode_produk']:<10}"
                f"{item['nama_produk']:<25}"
                f"{item['jumlah_batch']:>10}"
                f"{item['jumlah_produk']:>12}"
                f"{item['biaya_produksi']:>18,.0f}"
            )

        print("=" * 90)

    @staticmethod
    def tampilkan_ringkasan(total_produk, total_biaya):
        print("\n")
        print("=" * 50)
        print("RINGKASAN PRODUKSI")
        print("=" * 50)
        print(f"Total Produk Diproduksi : {total_produk}")
        print(f"Total Biaya Produksi    : Rp {total_biaya:,.0f}")
        print("=" * 50)

    @staticmethod
    def tampilkan_pesan(pesan):
        print(f"\n{pesan}")

    @staticmethod
    def tampilkan_error(error):
        print("\n")
        print("=" * 50)
        print("ERROR PRODUKSI")
        print("=" * 50)
        print(error)
        print("=" * 50)