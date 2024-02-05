from src.Caractere import Caractere

class PorteFerme(Caractere):
    #voir classe parenjte Caractere()
    def __init__(self):
        super().__init__(chr(21))  # symbole ""

    def traversable(self, joueur):
        return 0

    def enigme(self):
        return 1
    