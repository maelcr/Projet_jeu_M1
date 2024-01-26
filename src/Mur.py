from Caractere import Caractere

class Mur(Caractere):
    def __init__(self):
        super().__init__(chr(64))  # symbole "@"

    def traversable(self, joueur):
        return 0