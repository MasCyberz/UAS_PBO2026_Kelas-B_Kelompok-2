class ProfitService:

    def __init__(
        self,
        produk_service,
        resep_service,
        production_service
    ):
        self.produk_service = produk_service
        self.resep_service = resep_service
        self.production_service = production_service

    # HITUNG BIAYA PRODUKSI

    def hitung_biaya_produksi(
        self,
        kode_produk,
        jumlah_batch
    ):

        produk = self.produk_service.get_produk(
            kode_produk
        )

        if produk is None:
            raise ValueError("Produk tidak ditemukan.")

        biaya_per_batch = self.resep_service.hitung_harga_resep(
            kode_produk
        )

        return biaya_per_batch * jumlah_batch

    # HITUNG OMZET

    def hitung_omzet(
        self,
        kode_produk,
        jumlah_batch
    ):

        produk = self.produk_service.get_produk(
            kode_produk
        )

        if produk is None:
            raise ValueError("Produk tidak ditemukan.")

        jumlah_produk = (
            produk.batch_size
            * jumlah_batch
        )

        return jumlah_produk * produk.harga_jual

    # HITUNG LABA

    def hitung_laba(
        self,
        kode_produk,
        jumlah_batch
    ):

        omzet = self.hitung_omzet(
            kode_produk,
            jumlah_batch
        )

        biaya = self.hitung_biaya_produksi(
            kode_produk,
            jumlah_batch
        )

        return omzet - biaya

    # LAPORAN PRODUK

    def laporan_produk(
        self,
        kode_produk,
        jumlah_batch
    ):

        produk = self.produk_service.get_produk(
            kode_produk
        )

        if produk is None:
            raise ValueError("Produk tidak ditemukan.")

        jumlah_produk = (
            produk.batch_size
            * jumlah_batch
        )

        biaya = self.hitung_biaya_produksi(
            kode_produk,
            jumlah_batch
        )

        omzet = self.hitung_omzet(
            kode_produk,
            jumlah_batch
        )

        laba = omzet - biaya

        return {
            "kode_produk": produk.kode,
            "nama_produk": produk.nama,
            "jumlah_batch": jumlah_batch,
            "jumlah_produk": jumlah_produk,
            "harga_jual": produk.harga_jual,
            "biaya_produksi": biaya,
            "omzet": omzet,
            "laba": laba
        }

    # TOTAL LABA DARI RIWAYAT PRODUKSI

    def total_laba(self):

        total = 0

        riwayat = self.production_service.get_riwayat()

        for item in riwayat:

            total += self.hitung_laba(
                item["kode_produk"],
                item["jumlah_batch"]
            )

        return total

    # TOTAL OMZET

    def total_omzet(self):

        total = 0

        riwayat = self.production_service.get_riwayat()

        for item in riwayat:

            total += self.hitung_omzet(
                item["kode_produk"],
                item["jumlah_batch"]
            )

        return total

    # TOTAL BIAYA PRODUKSI

    def total_biaya_produksi(self):

        total = 0

        riwayat = self.production_service.get_riwayat()

        for item in riwayat:

            total += self.hitung_biaya_produksi(
                item["kode_produk"],
                item["jumlah_batch"]
            )

        return total

    # RINGKASAN KEUANGAN

    def ringkasan_keuangan(self):

        omzet = self.total_omzet()
        biaya = self.total_biaya_produksi()
        laba = omzet - biaya

        return {
            "total_omzet": omzet,
            "total_biaya": biaya,
            "total_laba": laba
        }
    
    def get_laporan_profit(self):
        hasil = {}

        riwayat = self.production_service.get_riwayat()

        for item in riwayat:

            kode = item["kode_produk"]

            produk = self.produk_service.get_produk(
                kode
            )

            if kode not in hasil:

                hasil[kode] = {
                    "kode_produk": kode,
                    "nama_produk": produk.nama,
                    "tanggal_terakhir": item["tanggal"],
                    "jumlah_batch": 0,
                    "jumlah_produk": 0,
                    "harga_jual": produk.harga_jual,
                    "biaya_produksi": 0,
                    "omzet": 0,
                    "laba": 0
                }
            hasil[kode]["tanggal_terakhir"] = item["tanggal"]

            hasil[kode]["jumlah_batch"] += (
                item["jumlah_batch"]
            )

            hasil[kode]["jumlah_produk"] += (
                item["jumlah_produk"]
            )

            hasil[kode]["biaya_produksi"] += (
                item["biaya_produksi"]
            )

            omzet = self.hitung_omzet(
                kode,
                item["jumlah_batch"]
            )

            hasil[kode]["omzet"] += omzet

            hasil[kode]["laba"] += (
                omzet - item["biaya_produksi"]
            )

        return list(hasil.values())