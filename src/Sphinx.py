from src.Caractere import Caractere

class Sphinx(Caractere):
    def __init__(self):
        super().__init__(chr(14))  # symbole ""

    def traversable(self, joueur):
        return 0
    
    """
    def boiteDialogue(self, joueur):
        return 1
    """
    def enigme(self):
        return 1