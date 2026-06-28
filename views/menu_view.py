from views.input_view import InputView
from views.produk_view import ProdukView
from views.production_view import ProductionView
from views.bahan_view import BahanView
from views.profit_view import ProfitView

class MenuView:
    def __init__(self, bakery):
        self.bakery = bakery

    def tampilkan_menu(self):

        print("\n")
        print("=" * 60)
        print("\n=== SISTEM MANAJEMEN HANARI BAKERY ===")
        print("=" * 60)
        print("1. Produk")
        print("2. Produksi")
        print("3. Bahan")
        print("4. Profit")
        print("0. Keluar")
        print("=" * 60)

    def run(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("Pilih menu : ")

            if pilihan == "1":
                ProdukView.menu(self.bakery)

            elif pilihan == "2":
                ProductionView.menu(self.bakery)

            elif pilihan == "3":
                BahanView.tampilkan_semua(
                    self.bakery.bahan_service.get_bahan()
                )

            elif pilihan == "4":
                ProfitView.menu(self.bakery)

            elif pilihan == "0":
                print("\nTerima kasih.")
                break

            else:
                print("Menu tidak tersedia.")