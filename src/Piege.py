from src.Caractere import Caractere

class Piege(Caractere):
    #voir classe parenjte Caractere()
    def __init__(self):
        super().__init__(chr(15))  # symbole ""

    def traversable(self, joueur):
        return 1
    
    def piege(self, joueur):
        joueur.update_health(-1)  # Le joueur perd un point de vie
        return 1