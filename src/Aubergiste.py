from src.Caractere import Caractere

class Aubergiste(Caractere):
    def __init__(self):
        super().__init__(chr(20))  # symbole ""

    def traversable(self, joueur):
        return 1
    
    def gagneVie(self, joueur):
        joueur.update_health(1)  
        return 1
        