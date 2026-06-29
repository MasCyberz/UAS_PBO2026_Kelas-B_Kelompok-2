from abc import ABC, abstractmethod

class IPemanggangan(ABC):
    #Interface untuk standarisasi proses pemanggangan (baking) di oven.
    
    @abstractmethod
    def panggang_adonan(self, suhu_celcius: int, durasi_menit: int) -> None:
    #Metode untuk mensimulasikan proses pemanggangan produk.
class Pemanggangan(ABC):
    @abstractmethod
    def pemanggangan(self):
        pass