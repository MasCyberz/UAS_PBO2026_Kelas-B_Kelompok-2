from services.bakery_service import BakeryService
from views.menu_view import MenuView


def main():
    bakery = BakeryService()
    menu = MenuView(bakery)
    menu.run()


if __name__ == "__main__":
    main()