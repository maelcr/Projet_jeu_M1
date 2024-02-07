from src.Caractere import Caractere

class BarriereGauche(Caractere):
    #voir classe parenjte Caractere()
    def __init__(self):
        super().__init__(chr(27))  # symbole ""

    def traversable(self, joueur):
         return 1
     
    def sens(self, joueur):
         return 1