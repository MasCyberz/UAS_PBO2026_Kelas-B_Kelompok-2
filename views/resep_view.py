from views.input_view import InputView


class RecipeView:

    @staticmethod
    def tampilkan_semua(daftar_resep):

        print("\n")
        print("=" * 70)
        print("DAFTAR RESEP")
        print("=" * 70)

        if not daftar_resep:
            print("Belum ada resep.")
            return

        for resep in daftar_resep:

            print(f"\n[{resep.kode}] {resep.nama}")

            for detail in resep.daftar_bahan:

                print(
                    f" - {detail.bahan.nama}"
                    f" ({detail.jumlah} {detail.bahan.satuan})"
                )

        print("=" * 70)

    @staticmethod
    def tampilkan_detail(resep):

        if resep is None:
            print("Resep tidak ditemukan.")
            return

        print("\n")
        print("=" * 60)
        print("DETAIL RESEP")
        print("=" * 60)

        print(f"Kode : {resep.kode}")
        print(f"Nama : {resep.nama}")

        print("\nDaftar Bahan")

        for detail in resep.daftar_bahan:

            print(
                f"- {detail.bahan.nama}"
                f" ({detail.jumlah} {detail.bahan.satuan})"
            )

        print("=" * 60)

    @staticmethod
    def input_resep():

        print("\nTambah Resep")

        return {
            "kode": InputView.input_string("Kode Resep"),
            "nama": InputView.input_string("Nama Resep")
        }

    @staticmethod
    def input_bahan_resep():

        print("\nTambah Bahan ke Resep")

        return (
            InputView.input_string("Kode Resep"),
            InputView.input_string("Kode Bahan"),
            InputView.input_float("Jumlah")
        )

    @staticmethod
    def input_update_bahan():

        print("\nUpdate Bahan Resep")

        return (
            InputView.input_string("Kode Resep"),
            InputView.input_string("Kode Bahan"),
            InputView.input_float("Jumlah Baru")
        )

    @staticmethod
    def tampilkan_harga(total):

        print(f"\nTotal Biaya Resep : Rp {total:,.0f}")

    @staticmethod
    def tampilkan_pesan(pesan):

        print(f"\n{pesan}")

    @staticmethod
    def tampilkan_error(error):

        print(f"\nError : {error}")