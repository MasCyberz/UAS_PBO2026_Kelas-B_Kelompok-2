from abc import ABC, abstractmethod
    
class Pengembangan(ABC):
    #Interface untuk standarisasi proses pengembangan (proofing) adonan.


    @abstractmethod
    def pengembangan(self):
        pass
    #Metode untuk mensimulasikan proses pengembangan adonan.