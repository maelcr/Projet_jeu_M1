from src.Caractere import Caractere

class PorteOuverte(Caractere):
    def __init__(self):
        super().__init__(chr(47))  # symbole "/"

    def traversable(self, joueur):
        return 1
    
 