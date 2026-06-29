from views.input_view import InputView
from models.resep import Resep


class RecipeView:

    # CONTROLLER / LOOP UTAMA

    @staticmethod
    def run(bakery):

        while True:

            pilihan = RecipeView.menu()

            try:

                if pilihan == "1":
                    daftar = bakery.resep_service.get_all_resep()
                    RecipeView.tampilkan_semua(daftar)

                elif pilihan == "2":
                    kode = RecipeView.input_kode_resep()
                    resep = bakery.resep_service.get_resep_by_code(kode)
                    RecipeView.tampilkan_detail(resep)

                elif pilihan == "3":
                    data = RecipeView.input_resep()
                    resep_baru = Resep(data["kode"], data["nama"], [])
                    bakery.resep_service.tambah_resep(resep_baru)
                    RecipeView.tampilkan_pesan("Resep berhasil ditambahkan.")

                elif pilihan == "4":
                    kode_resep, kode_bahan, jumlah = RecipeView.input_bahan_resep()
                    bakery.resep_service.tambah_bahan(kode_resep, kode_bahan, jumlah)
                    RecipeView.tampilkan_pesan("Bahan berhasil ditambahkan ke resep.")

                elif pilihan == "5":
                    kode_resep, kode_bahan, jumlah = RecipeView.input_update_bahan()
                    bakery.resep_service.update_bahan(kode_resep, kode_bahan, jumlah)
                    RecipeView.tampilkan_pesan("Bahan pada resep berhasil diperbarui.")

                elif pilihan == "6":
                    kode_resep, kode_bahan = RecipeView.input_hapus_bahan()
                    bakery.resep_service.hapus_bahan(kode_resep, kode_bahan)
                    RecipeView.tampilkan_pesan("Bahan berhasil dihapus dari resep.")

                elif pilihan == "7":
                    kode = RecipeView.input_hitung_harga()
                    total = bakery.resep_service.hitung_harga_resep(kode)
                    RecipeView.tampilkan_harga(total)

                elif pilihan == "8":
                    kode = RecipeView.input_hapus_resep()
                    bakery.resep_service.hapus_resep(kode)
                    RecipeView.tampilkan_pesan("Resep berhasil dihapus.")

                elif pilihan == "0":
                    break

                else:
                    print("\nMenu tidak tersedia.")

            except Exception as e:
                RecipeView.tampilkan_error(e)

    # MENU

    @staticmethod
    def menu():

        print("\n")
        print("=" * 60)
        print("MENU RESEP")
        print("=" * 60)
        print("1. Lihat Semua Resep")
        print("2. Lihat Detail Resep")
        print("3. Tambah Resep")
        print("4. Tambah Bahan ke Resep")
        print("5. Update Bahan pada Resep")
        print("6. Hapus Bahan dari Resep")
        print("7. Hitung Biaya Resep")
        print("8. Hapus Resep")
        print("0. Kembali")
        print("=" * 60)

        return InputView.input_string("Pilih Menu")

    # TAMPILKAN SEMUA RESEP

    @staticmethod
    def tampilkan_semua(daftar_resep):

        print("\n")
        print("=" * 70)
        print("DAFTAR RESEP")
        print("=" * 70)

        if not daftar_resep:
            print("Belum ada resep.")
            print("=" * 70)
            return

        for resep in daftar_resep:

            print(f"[{resep.kode}] {resep.nama}")

        print("=" * 70)

    # DETAIL RESEP

    @staticmethod
    def tampilkan_detail(resep):

        if resep is None:
            print("\nResep tidak ditemukan.")
            return

        print("\n")
        print("=" * 60)
        print("DETAIL RESEP")
        print("=" * 60)

        print(f"Kode Resep : {resep.kode}")
        print(f"Nama Resep : {resep.nama}")

        print("\nDaftar Bahan")

        nomor = 1

        for detail in resep.daftar_bahan:

            print(
                f"{nomor}. "
                f"{detail.bahan.nama}"
                f" ({detail.jumlah} {detail.bahan.satuan})"
            )

            nomor += 1

        print("=" * 60)

    # INPUT KODE RESEP

    @staticmethod
    def input_kode_resep():

        print("\nLihat Detail Resep")

        return InputView.input_string("Kode Resep")

    # TAMBAH RESEP

    @staticmethod
    def input_resep():

        print("\nTambah Resep")

        return {
            "kode": InputView.input_string("Kode Resep"),
            "nama": InputView.input_string("Nama Resep")
        }

    # TAMBAH BAHAN

    @staticmethod
    def input_bahan_resep():

        print("\nTambah Bahan ke Resep")

        return (
            InputView.input_string("Kode Resep"),
            InputView.input_string("Kode Bahan"),
            InputView.input_float("Jumlah")
        )

    # UPDATE BAHAN

    @staticmethod
    def input_update_bahan():

        print("\nUpdate Bahan Resep")

        return (
            InputView.input_string("Kode Resep"),
            InputView.input_string("Kode Bahan"),
            InputView.input_float("Jumlah Baru")
        )

    # HAPUS BAHAN

    @staticmethod
    def input_hapus_bahan():

        print("\nHapus Bahan dari Resep")

        return (
            InputView.input_string("Kode Resep"),
            InputView.input_string("Kode Bahan")
        )

    # HITUNG BIAYA RESEP

    @staticmethod
    def input_hitung_harga():

        print("\nHitung Biaya Resep")

        return InputView.input_string("Kode Resep")

    @staticmethod
    def tampilkan_harga(total):

        print("\n")
        print("=" * 60)
        print("BIAYA RESEP")
        print("=" * 60)
        print(f"Total Biaya Resep : Rp {total:,.0f}")
        print("=" * 60)

    # HAPUS RESEP

    @staticmethod
    def input_hapus_resep():

        print("\nHapus Resep")

        return InputView.input_string("Kode Resep")

    # PESAN

    @staticmethod
    def tampilkan_pesan(pesan):

        print("\n")
        print("=" * 60)
        print(pesan)
        print("=" * 60)

    # ERROR

    @staticmethod
    def tampilkan_error(error):

        print("=" * 50)
        print(f"Gagal : {error}")
        print("=" * 50)