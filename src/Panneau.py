from src.Caractere import Caractere

class Panneau(Caractere):
    def __init__(self):
        super().__init__(chr(63))  # symbole "?"

    def traversable(self, joueur):
        return 0