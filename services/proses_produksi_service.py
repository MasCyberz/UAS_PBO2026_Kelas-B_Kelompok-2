from datetime import datetime
from interfaces.pengadonan import Pengadonan
from interfaces.pengembangan import Pengembangan
from interfaces.pemanggangan import Pemanggangan
from interfaces.toping import Toping

class ProductionService:

    def __init__(
        self,
        produk_service,
        resep_service,
        bahan_service
    ):
        self.produk_service = produk_service
        self.resep_service = resep_service
        self.bahan_service = bahan_service

        # Menyimpan riwayat produksi
        self.riwayat_produksi = []

    # VALIDASI PRODUK

    def validasi_produk(self, kode_produk):

        produk = self.produk_service.get_produk(kode_produk)

        if produk is None:
            raise ValueError(
                "Produk tidak ditemukan."
            )

        return produk

    # VALIDASI RESEP

    def validasi_resep(self, produk):

        if produk.resep is None:
            raise ValueError(
                "Produk belum memiliki resep."
            )

        return produk.resep

    # VALIDASI JUMLAH BATCH

    def validasi_batch(self, jumlah_batch):

        if jumlah_batch <= 0:
            raise ValueError(
                "Jumlah batch harus lebih dari 0."
            )

    # CEK STOK SELURUH BAHAN

    def cek_stok_bahan(
        self,
        resep,
        jumlah_batch
    ):

        for detail in resep.daftar_bahan:

            kebutuhan = (
                detail.jumlah
                * jumlah_batch
            )

            tersedia = self.bahan_service.cek_stok(
                detail.bahan.kode,
                kebutuhan
            )

            if not tersedia:

                bahan = self.bahan_service.get_bahan_by_code(
                    detail.bahan.kode
                )

                raise ValueError(
                    f"Stok bahan '{bahan.nama}' tidak mencukupi.\n"
                    f"Dibutuhkan : {kebutuhan} {bahan.satuan}\n"
                    f"Tersedia   : {bahan.stok} {bahan.satuan}"
                )

        return True

    # KURANGI STOK

    def gunakan_bahan(
        self,
        resep,
        jumlah_batch
    ):

        for detail in resep.daftar_bahan:

            kebutuhan = (
                detail.jumlah
                * jumlah_batch
            )

            self.bahan_service.kurang_bahan(
                detail.bahan.kode,
                kebutuhan
            )

    # HITUNG TOTAL PRODUK

    def hitung_total_produk(
        self,
        produk,
        jumlah_batch
    ):

        return (
            produk.batch_size
            * jumlah_batch
        )

    # HITUNG BIAYA BAHAN

    def hitung_biaya_bahan(
        self,
        resep,
        jumlah_batch
    ):

        total = 0

        for detail in resep.daftar_bahan:

            total += (
                detail.bahan.harga
                * detail.jumlah
                * jumlah_batch
            )

        return total
    

    # Proses Produksi

    def jalankan_proses(self, produk):
        if isinstance(produk, Pengadonan):
            produk.pengadonan()

        if isinstance(produk, Pengembangan):
            produk.pengembangan()

        if isinstance(produk, Pemanggangan):
            produk.pemanggangan()

        if isinstance(produk, Toping):
            produk.topping()
            
    # PRODUKSI

    def produksi(self, kode_produk, jumlah_batch):

        # Validasi jumlah batch
        self.validasi_batch(jumlah_batch)

        # Ambil produk
        produk = self.validasi_produk(kode_produk)

        # Ambil resep
        resep = self.validasi_resep(produk)

        # Cek stok
        self.cek_stok_bahan(
            resep,
            jumlah_batch
        )

        # Jalankan proses produksi
        self.jalankan_proses(produk)

        # Kurangi stok bahan
        self.gunakan_bahan(
            resep,
            jumlah_batch
        )

        # Hitung total produk
        total_produk = self.hitung_total_produk(
            produk,
            jumlah_batch
        )

        # Hitung biaya produksi
        biaya_produksi = self.hitung_biaya_bahan(
            resep,
            jumlah_batch
        )

        hasil = {
            "tanggal": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "kode_produk": produk.kode,
            "nama_produk": produk.nama,
            "jumlah_batch": jumlah_batch,
            "jumlah_produk": total_produk,
            "biaya_produksi": biaya_produksi,
            "status": "Selesai"
        }

        self.riwayat_produksi.append(hasil)

        return hasil

    # RIWAYAT PRODUKSI

    def get_riwayat(self):
        return self.riwayat_produksi

    # TOTAL PRODUKSI

    def total_produksi(self):

        total = 0

        for item in self.riwayat_produksi:
            total += item["jumlah_produk"]

        return total

    # TOTAL BIAYA PRODUKSI

    def total_biaya_produksi(self):

        total = 0

        for item in self.riwayat_produksi:
            total += item["biaya_produksi"]

        return total

    # CARI RIWAYAT

    def cari_riwayat(self, kode_produk):

        hasil = []

        for item in self.riwayat_produksi:

            if item["kode_produk"] == kode_produk:
                hasil.append(item)

        return hasil

    # HAPUS RIWAYAT

    def hapus_riwayat(self):
        self.riwayat_produksi.clear()