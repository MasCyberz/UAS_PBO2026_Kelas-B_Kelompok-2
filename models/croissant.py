from models.bakery_product import BakeryProduct

class Croissant(BakeryProduct):
    def __init__(self):
        super().__init__("Crpissant", 12)

        self.resep = {
            "Tepung Terigu Protein Tinggi" : "500 gr",
            "Garam" : "10 gr",
            "Gula Pasir" : "60 gr",
            "Ragi Instan" : "10 gr",
            "Susu Cair Dingin" : "300ml",
            "Mentega Dingin" : "250 gr",
            "Telur (olesan)" : "1 butir"
        }