from models.bakery_product import BakeryProduct

class ButterCookies(BakeryProduct):
    def __init__(self):
        super().__init__("Butter Cookies", 40)

        self.resep = {
            "Tepung Terigu Protein Rendah" : "250 gr",
            "Butter/Margarin" : "200 gr",
            "Gula Halus" : "100 gr",
            "Tepung Maizena" : "40 gr",
            "Susu Bubuk" : "20 gr",
            "Kuning Telur" : "2 butir",
            "Ekstrak Vanili" : "1 sdt",
            "Topping Chocochips/Keju" : "50 gr",
        }