class InputView:

    @staticmethod
    def input_string(pesan):
        return input(f"{pesan}: ")

    @staticmethod
    def input_int(pesan):
        while True:
            try:
                return int(input(f"{pesan}: "))
            except ValueError:
                print("Input harus berupa angka.")

    @staticmethod
    def input_float(pesan):
        while True:
            try:
                return float(input(f"{pesan}: "))
            except ValueError:
                print("Input harus berupa angka.")

    @staticmethod
    def konfirmasi(pesan):
        return input(f"{pesan} (y/n): ").lower() == "y"