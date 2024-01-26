from Caractere import Caractere

class CaseVide(Caractere):
    def __init__(self):
        super().__init__(chr(46))  # symbole "."

    def traversable(self, joueur):
        return 1
    