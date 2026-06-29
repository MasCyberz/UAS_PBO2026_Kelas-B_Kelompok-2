from abc import ABC, abstractmethod

class Pemanggangan(ABC):
    #Interface untuk standarisasi proses pemanggangan (baking) di oven.

    @abstractmethod
    def pemanggangan(self):
        pass
    #Metode untuk mensimulasikan proses pemanggangan produk.
