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
        return None
    
    # Menambahkan bahan baru
    def add_bahan(self, kode, nama, satuan, stok, harga):
        if kode in self.bahan:
            raise ValueError(f"Bahan dengan kode {kode} sudah ada.")
        
        self.bahan[kode] = Bahan(kode, nama, satuan, stok, harga)
    
    # Mengupdate bahan
    def update_bahan(self, kode, nama=None, satuan=None, harga=None):
        bahan = self.get_bahan_by_code(kode)
        
        if bahan is None:
            raise ValueError(f"Bahan dengan kode {kode} tidak ditemukan.")
        
        if nama is not None:
            self.bahan[kode].nama = nama
        
        if satuan is not None:
            self.bahan[kode].satuan = satuan
        
        if harga is not None:
            self.bahan[kode].harga = harga
    
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
    
    def lihat_bahan(self, kode):
        print("=" * 60)
        print("DAFTAR BAHAN")
        print("=" * 60)
        
        bahan = self.get_bahan_by_code(kode)
        print(f"Kode\t\t: {bahan.kode:20}")
        print(f"Nama\t\t: {bahan.nama:20}")
        print(f"Satuan\t\t: {bahan.satuan:20}")
        print(f"Stok\t\t: {bahan.stok:20}")
        print(f"Harga\t\t: {bahan.harga:20}")