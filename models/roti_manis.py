from models.bakery_product import BakeryProduct

class RotiManis(BakeryProduck):
    def __init__(self):
        super().__init__("Roti Manis Coklat", 20)

        self.resep = {
            "Tepung Terigu" : "500 gr",
            "Gula Pasir" : "80 gr",
            "Ragi Instan" : "8 gr",
            "Susu Bubuk" : "25 gr",
            "Telur" : "1 butir" ,
            "Margarin" : "50 gr",
            "Air" : "250 ml" ,
            "Coklat Meses" : "150 gr"
        }