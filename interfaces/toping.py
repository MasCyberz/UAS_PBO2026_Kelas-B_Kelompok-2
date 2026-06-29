from abc import ABC, abstractmethod

class IToping(ABC):
#Interface untuk standarisasi proses pemberian topping pada kue.
    
    @abstractmethod
    def beri_topping(self, jenis_topping: str) -> None:
    #Metode untuk mensimulasikan proses pemberian topping.
        pass