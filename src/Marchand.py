from src.Caractere import Caractere

class Marchand(Caractere):
    #voir classe parenjte Caractere()
    def __init__(self):
        super().__init__(chr(77))  # symbole "M"

    def traversable(self, joueur):
        return 0
    """
    def boiteDialogue(self, joueur):
        return 1
    """