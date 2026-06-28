from views.input_view import InputView


class ProductionView:
    
    @staticmethod
    def menu(bakery):
        try:
            print("\n=== PRODUKSI ===")

            kode, batch = ProductionView.input_produksi()

            hasil = bakery.production_service.produksi(kode, batch)

            ProductionView.tampilkan_hasil(hasil)

        except Exception as e:
            ProductionView.tampilkan_error(e)

    @staticmethod
    def input_produksi():

        print("\n")
        print("=" * 50)
        print("PRODUKSI")
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