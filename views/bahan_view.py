from views.input_view import InputView


class BahanView:
    
    @staticmethod
    def menu(bakery):

        while True:

            print("\n")
            print("=" * 60)
            print("MENU BAHAN")
            print("=" * 60)
            print("1. Lihat Semua Bahan")
            print("2. Detail Bahan")
            print("3. Tambah Bahan")
            print("4. Update Bahan")
            print("5. Tambah Stok")
            print("6. Kurang Stok")
            print("7. Hapus Bahan")
            print("0. Kembali")
            print("=" * 60)

            pilihan = InputView.input_string("Pilih Menu")

            try:

                if pilihan == "1":

                    daftar = bakery.bahan_service.get_bahan()
                    BahanView.tampilkan_semua(daftar)

                elif pilihan == "2":

                    kode = BahanView.input_kode()

                    bahan = bakery.bahan_service.get_bahan_by_code(kode)

                    BahanView.tampilkan_detail(bahan)

                elif pilihan == "3":

                    data = BahanView.input_bahan()

                    bakery.bahan_service.add_bahan(
                        data["kode"],
                        data["nama"],
                        data["satuan"],
                        data["stok"],
                        data["harga"]
                    )

                    BahanView.tampilkan_pesan(
                        "Bahan berhasil ditambahkan."
                    )

                elif pilihan == "4":

                    data = BahanView.input_update()

                    bakery.bahan_service.update_bahan(
                        data["kode"],
                        data["nama"],
                        data["satuan"],
                        data["harga"]
                    )

                    BahanView.tampilkan_pesan(
                        "Data bahan berhasil diperbarui."
                    )

                elif pilihan == "5":

                    kode, jumlah = BahanView.input_tambah_stok()

                    bakery.bahan_service.tambah_stok(
                        kode,
                        jumlah
                    )

                    BahanView.tampilkan_pesan(
                        "Stok berhasil ditambahkan."
                    )

                elif pilihan == "6":

                    kode, jumlah = BahanView.input_kurang_stok()
                    bakery.bahan_service.kurang_bahan(
                        kode,
                        jumlah
                    )

                    BahanView.tampilkan_pesan(
                        "Stok berhasil dikurangi."
                    )
                    
                elif pilihan == "7":

                    kode = BahanView.input_hapus()

                    bakery.bahan_service.hapus_bahan(kode)

                    BahanView.tampilkan_pesan(
                        "Bahan berhasil dihapus."
                    )

                elif pilihan == "0":
                    break

                else:
                    print("\nMenu tidak tersedia.")

            except Exception as e:
                BahanView.tampilkan_error(e)

    @staticmethod
    def tampilkan_semua(daftar_bahan):

        print("\n")
        print("=" * 70)
        print("DAFTAR BAHAN")
        print("=" * 70)

        if not daftar_bahan:
            print("Belum ada data bahan.")
            print("=" * 70)
            return

        print(
            f"{'Kode':<10}"
            f"{'Nama':<25}"
            f"{'Stok':>10}"
            f"{'Satuan':>10}"
            f"{'Harga':>15}"
        )

        print("-" * 70)

        for bahan in daftar_bahan:
            print(
                f"{bahan.kode:<10}"
                f"{bahan.nama:<25}"
                f"{bahan.stok:>10.2f}"
                f"{bahan.satuan:>10}"
                f"{bahan.harga:>15,.2f}"
            )

        print("=" * 70)

    @staticmethod
    def tampilkan_detail(bahan):

        if bahan is None:
            print("Bahan tidak ditemukan.")
            return

        print("\n")
        print("=" * 50)
        print("DETAIL BAHAN")
        print("=" * 50)
        print(f"Kode    : {bahan.kode}")
        print(f"Nama    : {bahan.nama}")
        print(f"Stok    : {bahan.stok}")
        print(f"Satuan  : {bahan.satuan}")
        print(f"Harga   : Rp {bahan.harga:,.0f}")
        print("=" * 50)

    @staticmethod
    def input_kode():

        print("\nDetail Bahan")

        return InputView.input_string(
            "Kode Bahan"
        )

    @staticmethod
    def input_bahan():

        print("\n")
        print("=" * 50)
        print("\nTambah Bahan")
        print("=" * 50)

        return {
            "kode": InputView.input_string("Kode"),
            "nama": InputView.input_string("Nama"),
            "satuan": InputView.input_string("Satuan"),
            "stok": InputView.input_float("Stok"),
            "harga": InputView.input_float("Harga")
        }

    @staticmethod
    def input_update():

        print("\n")
        print("=" * 50)
        print("\nUpdate Bahan")
        print("=" * 50)

        return {
            "kode": InputView.input_string("Kode"),
            "nama": InputView.input_string("Nama Baru"),
            "satuan": InputView.input_string("Satuan Baru"),
            "harga": InputView.input_float("Harga Baru")
        }

    @staticmethod
    def input_tambah_stok():
        
        print("\n")
        print("=" * 50)
        print("Tambah Stok")
        print("=" * 50)

        return (
            InputView.input_string("Kode Bahan"),
            InputView.input_float("Jumlah Stok")
        )
    
    
    @staticmethod
    def input_kurang_stok():

        print("\nKurangi Stok Bahan")

        return (
            InputView.input_string("Kode Bahan"),
            InputView.input_float("Jumlah Stok")
        )
        
    @staticmethod
    def input_hapus():

        print("\nHapus Bahan")

        return InputView.input_string(
            "Kode Bahan"
        )

    @staticmethod
    def tampilkan_pesan(pesan):

        print(f"\n{pesan}")

    @staticmethod
    def tampilkan_error(error):

        print("=" * 50)
        print(f"Gagal : {error}")
        print("=" * 50)