from Caractere import Caractere

class PiegeMortel(Caractere):
    def __init__(self):
        super().__init__(chr(19))  # symbole ""

    def traversable(self, joueur):
        return 1
    
    def piege(self, joueur):
        joueur.update_health(-10)  
        return 1