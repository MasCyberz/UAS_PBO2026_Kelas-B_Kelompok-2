from data.data_bahan import data_awal_bahan
from models.bahan import Bahan

class BahanServices:
    def __init__(self):
        self.bahan = data_awal_bahan()

    # Mengembalikan daftar bahan
    def get_bahan(self):
        
        return list(self.bahan.values())
    
    # Mengembalikan bahan berdasarkan nama
    def get_bahan_by_name(self, nama_bahan):
        return self.bahan[nama_bahan]
    
    # Mengembalikan bahan berdasarkan kode
    def get_bahan_by_code(self, kode):
        for bahan in self.bahan.values():
            if bahan.kode == kode:
                return bahan
        
        raise ValueError(f"Bahan dengan kode {kode} tidak ditemukan.")
    
    # Menambahkan bahan baru
    def add_bahan(self, kode, nama, satuan, stok, harga):
        
        if any(bahan.kode == kode for bahan in self.bahan.values()):
            raise ValueError(f"Bahan dengan kode {kode} sudah ada.")
        
        self.bahan[kode] = Bahan(kode, nama, satuan, stok, harga)
    
    # Mengupdate bahan
    def update_bahan(self, kode, nama=None, satuan=None, harga=None):
        bahan = self.get_bahan_by_code(kode)
        
        if nama:
            bahan.nama = nama

        if satuan:
            bahan.satuan = satuan

        if harga:
            bahan.harga = harga
            
        return bahan
    
    # Hapus bahan
    def hapus_bahan(self, kode):
        bahan = self.get_bahan_by_code(kode)

        if bahan is None:
            raise ValueError(
                f"Bahan dengan kode {kode} tidak ditemukan."
            )

        for key, value in self.bahan.items():
            if value.kode == kode:
                del self.bahan[key]
                return

    # Stok bahan
    def tambah_stok(self, kode, jumlah):
        bahan = self.get_bahan_by_code(kode)

        if bahan is None:
            raise ValueError(f"Bahan dengan kode {kode} tidak ditemukan.")
        
        bahan.stok += jumlah
        
    def kurang_bahan(self, kode, jumlah):
        bahan = self.get_bahan_by_code(kode)
        
        if bahan is None:
            raise ValueError("Bahan tidak ditemukan.")
        
        if bahan.stok < jumlah:
            raise ValueError("Stok bahan tidak mencukupi.")
        
        bahan.stok -= jumlah
        
    def cek_stok(self, kode, jumlah):
        bahan = self.get_bahan_by_code(kode)

        if bahan is None:
            return False
        
        return bahan.stok >= jumlah