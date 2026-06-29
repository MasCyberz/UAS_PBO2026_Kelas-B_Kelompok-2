class ProfitView:
    @staticmethod
    def menu(bakery):
        try:
            print("\n=== LAPORAN PROFIT ===")

            kode = input("Kode Produk : ")
            batch = int(input("Jumlah Batch : "))

            laporan = bakery.profit_service.laporan_produk(kode, batch)
            ringkasan = bakery.profit_service.ringkasan_keuangan()

            ProfitView.tampilkan_laporan(laporan)
            ProfitView.tampilkan_ringkasan(ringkasan)

        except Exception as e:
            ProfitView.tampilkan_error(e)
    @staticmethod
    def tampilkan_laporan(data):

        print("\n")
        print("=" * 70)
        print("LAPORAN KEUNTUNGAN")
        print("=" * 70)

        print(f"Kode Produk      : {data['kode_produk']}")
        print(f"Nama Produk      : {data['nama_produk']}")
        print(f"Jumlah Batch     : {data['jumlah_batch']}")
        print(f"Jumlah Produk    : {data['jumlah_produk']}")
        print(f"Harga Jual       : Rp {data['harga_jual']:,.0f}")
        print(f"Biaya Produksi   : Rp {data['biaya_produksi']:,.0f}")
        print(f"Omzet            : Rp {data['omzet']:,.0f}")
        print(f"Laba             : Rp {data['laba']:,.0f}")

        print("=" * 70)

    @staticmethod
    def tampilkan_ringkasan(data):

        print("\n")
        print("=" * 70)
        print("RINGKASAN KEUANGAN")
        print("=" * 70)

        print(f"Total Omzet          : Rp {data['total_omzet']:,.0f}")
        print(f"Total Biaya Produksi : Rp {data['total_biaya']:,.0f}")
        print(f"Total Laba           : Rp {data['total_laba']:,.0f}")

        print("=" * 70)

    @staticmethod
    def tampilkan_error(error):

        print("\n")
        print("=" * 60)
        print("ERROR")
        print("=" * 60)
        print(error)
        print("=" * 60)