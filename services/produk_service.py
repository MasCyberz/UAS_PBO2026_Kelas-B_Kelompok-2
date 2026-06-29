from data.data_produk import data_awal_produk

from models.roti_manis import RotiManis
from models.croissant import Croissant
from models.butter_cookies import ButterCookies
from models.muffin import Muffin

class ProdukService:
    PRODUCT_CLASSES = {
        "roti_manis": RotiManis,
        "croissant": Croissant,
        "butter_cookie": ButterCookies,
        "muffin": Muffin
    }
    
    def __init__(self, resep_service):
        self.resep_service = resep_service
        self.produk = data_awal_produk(
            self.resep_service.resep
            )
        
    # Mengembalikan semua produk
    def get_all_produk(self):
        return list(self.produk.values())
    
    # Mengembalikan produk berdasarkan kode
    def get_produk(self, kode_produk):
        return self.produk.get(kode_produk)
    
    # Mengembalikan produk berdaasarkan nama
    def get_produk_by_name(self, nama):
        for produk in self.produk.values():
            if produk.nama.lower() == nama.lower():
                return produk
        
        return None
    
    # Menambahkan produk baru
    def tambah_produk(self, data):
        jenis = data["jenis"]
        kode = data["kode"]
        nama = data["nama"]
        harga_jual = data["harga_jual"]
        batch_size = data["batch_size"]
        resep = data["resep"]

        if kode in self.produk:
            raise ValueError("Kode produk sudah digunakan.")
        
        product_class = self.PRODUCT_CLASSES.get(
            jenis.lower()
        )
        
        if product_class is None:
            raise ValueError("Jenis produk tidak valid.")
        
        produk = product_class(
            kode, 
            nama, 
            harga_jual, 
            batch_size, 
            resep)
        self.produk[kode] = produk
        
    # Update produk
    def update_produk(self, kode, nama=None, harga_jual=None, batch_size=None):
        produk = self.get_produk(kode)
        
        if produk is None:
            raise ValueError("Produk tidak ditemukan.")

        if nama is not None:
            produk.nama = nama

        if harga_jual is not None:
            produk.harga_jual = harga_jual
            
        if batch_size is not None:
            produk.batch_size = batch_size
        
    # Menghapus produk
    def delete_produk(self, kode):
        produk = self.get_produk(kode)
        
        if produk is None:
            raise ValueError("Produk tidak ditemukan.")
        
        del self.produk[kode]
        
    # Resep
    def ganti_resep(self, kode_produk, kode_resep):
        produk = self.get_produk(kode_produk)
        
        if produk is None:
            raise ValueError("Produk tidak ditemukan.")
        
        resep = self.resep_service.get_resep(kode_resep)

        if resep is None:
            raise ValueError("Resep tidak ditemukan.")
        
        produk.resep = resep
        
    # Filter
    def get_produk_by_type(self, jenis):
        hasil = []

        for produk in self.produk.values():
            if produk.__class__.__name__.lower() == jenis.lower():
                hasil.append(produk)

        return hasil
    
    # Search
    def search_produk(self, keyword):
        hasil = []

        keyword = keyword.lower()

        for produk in self.produk.values():

            if (
                keyword in produk.kode.lower()
                or
                keyword in produk.nama.lower()
            ):
                hasil.append(produk)

        return hasil
    
    # Validation
    def produk_tersdia(
        self,
        kode
    ):

        return kode in self.produk
    
    # Total

    def total_produk(self):
        return len(self.produk)