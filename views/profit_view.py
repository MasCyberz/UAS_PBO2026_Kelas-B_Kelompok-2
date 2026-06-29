class ProfitView:
    @staticmethod
    def menu(bakery):
        while True:
            try:

                print("\n=== MENU PROFIT ===")
                print("1. Laporan Profit Produk")
                print("2. Ringkasan Keuangan")
                print("0. Kembali")

                pilih = input("Pilih menu : ")

                if pilih == "1":

                    data = bakery.profit_service.get_laporan_profit()

                    if not data:
                        raise ValueError(
                            "Belum ada data produksi."
                        )

                    print("\n=== DAFTAR PRODUK ===")

                    for i, item in enumerate(data, start=1):
                        print(
                            f"{i}. "
                            f"{item['kode_produk']} - "
                            f"{item['nama_produk']} "
                            f"({item['jumlah_batch']} Batch)"
                        )

                    nomor = int(input("\nPilih Produk : "))

                    if nomor < 1 or nomor > len(data):
                        raise ValueError(
                            "Pilihan tidak valid."
                        )

                    laporan = data[nomor - 1]

                    ProfitView.tampilkan_laporan(
                        laporan
                    )

                elif pilih == "2":

                    ringkasan = (
                        bakery.profit_service
                        .ringkasan_keuangan()
                    )

                    ProfitView.tampilkan_ringkasan(
                        ringkasan
                    )

                elif pilih == "0":
                    break

                else:
                    print("Menu tidak tersedia.")

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

        print("=" * 50)
        print(f"Gagal : {error}")
        print("=" * 50)