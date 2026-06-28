from models.roti_manis import RotiManis
from models.croissant import Croissant
from models.butter_cookies import ButterCookies
from models.muffin import Muffin


def data_awal_produk(recipes):

    products = {}

    products["RM001"] = RotiManis(
        kode="RM001",
        nama="Roti Manis",
        harga_jual=8000,
        batch_size=10,
        resep=recipes["RM001"]
    )

    products["CR001"] = Croissant(
        kode="CR001",
        nama="Croissant",
        harga_jual=15000,
        batch_size=10,
        resep=recipes["CR001"]
    )

    products["BC001"] = ButterCookies(
        kode="BC001",
        nama="Butter Cookies",
        harga_jual=25000,
        batch_size=20,
        resep=recipes["BC001"]
    )

    products["MF001"] = Muffin(
        kode="MF001",
        nama="Muffin",
        harga_jual=12000,
        batch_size=10,
        resep=recipes["MF001"]
    )

    return products