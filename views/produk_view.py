from views.input_view import InputView


class ProdukView:
    @staticmethod
    def menu(bakery):

        while True:
            print("\n=== MENU PRODUK ===")
            print("1. Tambah Produk")
            print("2. Lihat Semua Produk")
            print("3. Update Produk")
            print("4. Hapus Produk")
            print("0. Kembali")

            pilihan = input("Pilih: ")

            if pilihan == "1":
                ProdukView.tambah_produk(bakery)

            elif pilihan == "2":
                ProdukView.tampilkan_semua(
                    bakery.produk_service.get_all_produk()
                )

            elif pilihan == "3":
                ProdukView.update_produk(bakery)

            elif pilihan == "4":
                ProdukView.hapus_produk(bakery)

            elif pilihan == "0":
                break

            else:
                print("Menu tidak valid")

    @staticmethod
    def tampilkan_semua(daftar_produk):

        print("\n")
        print("=" * 90)
        print("DAFTAR PRODUK")
        print("=" * 90)

        if not daftar_produk:
            print("Belum ada produk.")
            return

        print(
            f"{'Kode':<10}"
            f"{'Nama':<25}"
            f"{'Harga':>15}"
            f"{'Batch':>12}"
            f"{'Resep':>20}"
        )

        print("-" * 90)

        for produk in daftar_produk:

            nama_resep = "-"

            if produk.resep is not None:
                nama_resep = produk.resep.nama

            print(
                f"{produk.kode:<10}"
                f"{produk.nama:<25}"
                f"{produk.harga_jual:>15,.0f}"
                f"{produk.batch_size:>12}"
                f"{nama_resep:>20}"
            )

        print("=" * 90)

    @staticmethod
    def tampilkan_detail(produk):

        if produk is None:
            print("Produk tidak ditemukan.")
            return

        print("\n")
        print("=" * 60)
        print("DETAIL PRODUK")
        print("=" * 60)

        print(f"Kode           : {produk.kode}")
        print(f"Nama           : {produk.nama}")
        print(f"Harga Jual     : Rp {produk.harga_jual:,.0f}")
        print(f"Batch Size     : {produk.batch_size}")
        if produk.resep:
            print(f"Resep          : {produk.resep.nama}")
        else:
            print("Resep          : -")

        print("=" * 60)

    @staticmethod
    def input_produk():

        print("\nTambah Produk")

        return {
            "jenis": InputView.input_string("Jenis Produk"),
            "kode": InputView.input_string("Kode Produk"),
            "nama": InputView.input_string("Nama Produk"),
            "harga_jual": InputView.input_float("Harga Jual"),
            "batch_size": InputView.input_int("Batch Size"),
            "kode_resep": InputView.input_string("Kode Resep")
        }
    
    @staticmethod
    def tambah_produk(bakery):

        try:
            print("\n=== TAMBAH PRODUK ===")

            data = ProdukView.input_produk()

            kode_resep = data["kode_resep"]

            # cek resep
            resep = bakery.resep_service.get_resep_by_code(kode_resep)

            if resep is None:

                print("\nResep tidak ditemukan.")
                pilihan = input("Buat resep baru? (y/n): ").lower()

                if pilihan == "y":

                    nama_resep = InputView.input_string("Nama Resep")

                    resep = bakery.resep_service.tambah_resep({
                        "kode": kode_resep,
                        "nama": nama_resep
                    })

                    print("Resep berhasil dibuat.")

                else:
                    print("Produk akan dibuat TANPA resep.")
                    resep = None

            # masukkan object resep ke data
            data["resep"] = resep

            bakery.produk_service.tambah_produk(data)

            print("Produk berhasil ditambahkan.")

        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def input_update():

        print("\nUpdate Produk")

        return {
            "kode": InputView.input_string("Kode Produk"),
            "nama": InputView.input_string("Nama Baru"),
            "harga_jual": InputView.input_float("Harga Baru"),
            "batch_size": InputView.input_int("Batch Size Baru")
        }

    @staticmethod
    def input_ganti_resep():

        print("\nGanti Resep Produk")

        return (
            InputView.input_string("Kode Produk"),
            InputView.input_string("Kode Resep Baru")
        )

    @staticmethod
    def tampilkan_pesan(pesan):
        print(f"\n{pesan}")

    @staticmethod
    def tampilkan_error(error):
        print("=" * 50)
        print(f"\Gagal : {error}")
        print("=" * 50)