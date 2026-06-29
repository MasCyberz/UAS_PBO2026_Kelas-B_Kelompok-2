from abc import ABC, abstractmethod

class IPengembangan(ABC):
    #Interface untuk standarisasi proses pengembangan (proofing) adonan.
    
    @abstractmethod
    def kembangkan_adonan(self, durasi_menit: int) -> None:
    #Metode untuk mensimulasikan proses pengembangan adonan.
class Pengembangan(ABC):

    @abstractmethod
    def pengembangan(self):
        pass