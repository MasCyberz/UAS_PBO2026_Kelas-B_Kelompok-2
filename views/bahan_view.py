from views.input_view import InputView


class BahanView:

    @staticmethod
    def tampilkan_semua(daftar_bahan):

        print("\n")
        print("=" * 70)
        print("DAFTAR BAHAN")
        print("=" * 70)

        if not daftar_bahan:
            print("Belum ada data bahan.")
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
    def input_bahan():

        print("\nTambah Bahan")

        return {
            "kode": InputView.input_string("Kode"),
            "nama": InputView.input_string("Nama"),
            "satuan": InputView.input_string("Satuan"),
            "stok": InputView.input_float("Stok"),
            "harga": InputView.input_float("Harga")
        }

    @staticmethod
    def input_update():

        print("\nUpdate Bahan")

        return {
            "kode": InputView.input_string("Kode"),
            "nama": InputView.input_string("Nama Baru"),
            "satuan": InputView.input_string("Satuan Baru"),
            "harga": InputView.input_float("Harga Baru")
        }

    @staticmethod
    def input_tambah_stok():

        return (
            InputView.input_string("Kode Bahan"),
            InputView.input_float("Jumlah Stok")
        )

    @staticmethod
    def tampilkan_pesan(pesan):

        print(f"\n{pesan}")

    @staticmethod
    def tampilkan_error(error):

        print(f"\nError : {error}")