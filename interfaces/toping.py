from abc import ABC, abstractmethod

class Toping(ABC):
#Interface untuk standarisasi proses pemberian topping pada kue.

    @abstractmethod
    def toping(self):
        pass
    #Metode untuk mensimulasikan proses pemberian topping.
