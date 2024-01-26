from src.Caractere import Caractere

class EntreeGrotte(Caractere):
    def __init__(self):
        super().__init__(chr(23))  # symbole ""

    def traversable(self, joueur):
        return 1
    
    def ending(self, joueur):
        return 1