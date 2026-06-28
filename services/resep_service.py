from data.data_resep import data_awal_resep
from models.detail_resep import DetailResep

class ResepService:
    def __init__(self, bahan_service):
        self.bahan_service = bahan_service
        self.resep = data_awal_resep(
            self.bahan_service.bahan
        )
        
    # Mengembalikan data resep
    def get_all_resep(self):
        return list(self.resep.values())
    
    # Mengembalikan data resep berdasarkan kode
    def get_resep_by_code(self, kode):
        return self.resep.get(kode)
    
    # Membuat resep baru
    def tambah_resep(self, resep):
        if resep.kode in self.resep:
            raise ValueError(f"Resep dengan kode {resep.kode} sudah ada.")
        
        self.resep[resep.kode_produk] = resep

    # Update resep
    def update_resep(self, resep, kode_produk, bahan_baru):
        resep = self.get_resep(kode_produk)
        
        if resep is None:
            raise ValueError("Resep tidak ditemukan.")
        
        resep.daftar_bahan = bahan_baru
        
    # Hapus resep
    def hapus_resep(self, kode_produk):
        resep = self.get_resep(kode_produk)
        
        if resep is None:
            raise ValueError("Resep tidak ditemukan.")
        
        del self.resep[kode_produk]
        
    # Tambah bahan ke resep
    def tambah_bahan(self, kode_produk, kode_bahan, jumlah):
        resep = self.get_resep(kode_produk)
        
        if resep is None:
            raise ValueError("Resep tidak ditemukan.")
        
        bahan = self.bahan_service.get_bahan_by_code(kode_bahan)
        
        if bahan is None:
            raise ValueError("Bahan tidak ditemukan.")
        
        detail = DetailResep(bahan,jumlah)

        resep.daftar_bahan.append(detail)
    
    # Update bahan di resep
    def update_bahan(self, kode_produk, kode_bahan, jumlah):
        resep = self.get_resep(kode_produk)
        
        if resep is None:
            raise ValueError("Resep tidak ditemukan.")
        
        bahan = self.bahan_service.get_bahan_by_code(kode_bahan)
        
        if bahan is None:
            raise ValueError("Bahan tidak ditemukan.")
        
        for detail in resep.daftar_bahan:
            if detail.bahan.kode == kode_bahan:
                detail.jumlah = jumlah
                return
        
        raise ValueError("Bahan tidak ditemukan di dalam resep.")
        
    # Hapus bahan di resep
    def hapus_bahan(self, kode_produk, kode_bahan):
        resep = self.get_resep(kode_produk)
        
        if resep is None:
            raise ValueError("Resep tidak ditemukan.")
        
        bahan = self.bahan_service.get_bahan_by_code(kode_bahan)
        
        if bahan is None:
            raise ValueError("Bahan tidak ditemukan.")
        
        for detail in resep.daftar_bahan:
            if detail.bahan.kode == kode_bahan:
                resep.daftar_bahan.remove(detail)
                return
        
        raise ValueError("Bahan tidak ditemukan di dalam resep.")
        
    # Perhitungan harga resep
    def hitung_harga_resep(self, kode_produk):
        resep = self.get_resep(kode_produk)
        
        if resep is None:
            raise ValueError("Resep tidak ditemukan.")
        
        total_harga = 0
        
        for detail in resep.daftar_bahan:
            total_harga += (
                detail.bahan.harga * detail.jumlah
            )
        
        return total_harga