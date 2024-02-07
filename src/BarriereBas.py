from src.Caractere import Caractere

class BarriereBas(Caractere):
    #voir classe parenjte Caractere()
    def __init__(self):
        super().__init__(chr(27))  

    def traversable(self, joueur):
         return 1
     
    def sens(self, joueur):
         return 3