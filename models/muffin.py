from models.bakery_product import BakeryProduct

class Muffin(BakeryProduct):
    def __init__(self):
        super().__init__("Muffin", 12)

        self.resep = {
            "Telur" : "2 butir",
            "Susu UHT Cair" : "100 ml",
            "Minyak Goreng/Margarin Leleh" : "100 gr",
            "Tepung Terigu" : "200 gr",
            "Gula Pasir" : "100 gr",
            "Baking Powder" : "1 sdt",
            "Baking Soda" : "1/2 sdt",
            "Garam" : "1/4 sdt",
            "Topping Chocochips" : "100 gr",
            "Topping Pasta Vanila/Vanili Bubuk" : "1 sdt",
        }
