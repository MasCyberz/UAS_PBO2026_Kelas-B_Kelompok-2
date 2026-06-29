from views.input_view import InputView
from views.produk_view import ProdukView
from views.production_view import ProductionView
from views.bahan_view import BahanView
from views.profit_view import ProfitView
from views.resep_view import RecipeView

class MenuView:
    def __init__(self, bakery):
        self.bakery = bakery

    def tampilkan_menu(self):

        print("\n")
        print("=" * 60)
        print("=== SISTEM MANAJEMEN HANARI BAKERY ===")
        print("=" * 60)
        print("1. Produk")
        print("2. Resep")
        print("3. Produksi")
        print("4. Bahan")
        print("5. Profit")
        print("0. Keluar")
        print("=" * 60)

    def run(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("Pilih menu : ")

            if pilihan == "1":
                ProdukView.menu(self.bakery)

            elif pilihan == "2":
                RecipeView.run(self.bakery)

            elif pilihan == "3":
                ProductionView.menu(self.bakery)
                
            elif pilihan == "4":
                BahanView.menu(self.bakery)

            elif pilihan == "5":
                ProfitView.menu(self.bakery)

            elif pilihan == "0":
                print("\nTerima kasih.")
                break

            else:
                print("Menu tidak tersedia.")